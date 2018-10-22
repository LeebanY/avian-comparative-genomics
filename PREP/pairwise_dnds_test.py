from qsub import q_sub #Change to qsub when submitting.
import os
import sys

#Correct version

# locations
if len(sys.argv) != 5:
        print("Error.  There should be 5 inputs. Directory with pyhlip files, output directory, a tree file, and the codeml.ctl")
        quit()
#File locations - refer to this.
trimmed_files = sys.argv[1] #prepped_files
out_dir = sys.argv[2] #pairwise_dnds_output
tree_file = sys.argv[3] #don't need
codeml_ctl = sys.argv[4] #masters_script

#Create a list to put all the phylip files in.
trimmed_files_list = []
for phy in os.listdir(trimmed_files):
    if phy.endswith(".phylip"):
        trimmed_files_list.append(trimmed_files + phy)

#print("checkpoint 1 - list has been made")
cmd_list = []

#Next step: editing the codeml.ctl file in a loop. !Problem at this step - doesn't want to open file in write mode!
control_file = open(codeml_ctl)
control_file_contents = control_file.read()
control_file.close()
control_file_contents = control_file_contents.replace("stewart.trees", str(tree_file))

#print("test to see if within loop is problem")
for phylip_file in trimmed_files_list:

    # gets beginning of file name without input directory for output naming
    file_basename = phylip_file.split('/')[-1].replace('.phylip', '')

    new_control_file_contents = control_file_contents.replace("stewart.aa", phylip_file)
    out_name = out_dir + file_basename + '_dnds.phy'
    new_control_file_contents = new_control_file_contents.replace('mlc', out_name)

    # open new control file
    new_ctl_name = out_dir + file_basename + '_codeml.ctl'
    with open(new_ctl_name, 'w') as new_ctl:
        print(new_control_file_contents, file=new_ctl)

    codeml_cmd = '/data/bop17lhy/masters_scripts/codeml {}'.format(new_ctl_name)

    cmd_list.append(codeml_cmd)


#  Binning
for i in range(0, len(cmd_list), 100):
    bin_cmds = cmd_list[i:i+100]
    bin_outs = out_dir + 'jobs' + str(i) + '_to_' + str(i+100)
    #Change below to qsub when you want to submit.
    q_sub(bin_cmds, out=bin_outs)