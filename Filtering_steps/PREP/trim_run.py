from qsub import q_sub
import os
import sys

# locations
fas_dir = '/data/bop17lhy/sequences/PIPELINE_THREE/Filters/TEST/phylip_files/'
#seq_dir = ''
out_dir = '/data/bop17lhy/sequences/PIPELINE_THREE/Filters/TEST/trimal_fasta/'

# readble way
# read input files in
fas_list = []

for fas in os.listdir(fas_dir):
    if fas.endswith(".phylip"):
        fas_list.append(fas)

#print(fas_list)
# seq_list = []
#
# for seq in os.listdir(seq_dir):
#     if seq.endswith(".cds"):
#         seq_list.append(seq)

# list comprehension
# file_list = [fas for fas in os.listdir(in_dir) if fas.endswith(".fas")]

# process the files
cmd_list = []
for i in range(0, len(fas_list)):
    fas_file = fas_dir + fas_list[i]
    #seq_file = seq_dir + seq_list[i]
    #print(fas_file)

    # replaces .fas with .phylip, make list by cutting on '/', [-1] takes last item of list - the filename
    out_name = fas_file.replace('.phylip', '.fas').split('/')[-1]
    out_file = out_dir + out_name

    # print(fas_file, seq_file, out_file)
    trimal_cmd = ('/data/bop17lhy/trimal/source/trimal '
                  '-in {} -out {}'
                  ' -fasta').format(fas_file, out_file)
    cmd_list.append(trimal_cmd)


    #print(fas_file, out_file)
#     #subprocess.call(trimal_cmd, shell=True)
#
# submit bins of jobs
for i in range(0, len(cmd_list), 100):
    bin_cmds = cmd_list[i:i+100]
    bin_outs = out_dir + 'jobs' + str(i) + str(i+100)

    q_sub(bin_cmds, out=bin_outs)

