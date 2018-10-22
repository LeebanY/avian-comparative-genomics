#from qsub import q_sub #Change to qsub when submitting.
from __future__ import print_function
import os
import sys

# sys.argv returns commandline ie python script_name.py item1 item2 item3 in a list

# locations
if len(sys.argv) < 3:
    print('Missing arguments\nUsage: zorro_run.py fasta_directory/ output_directory/')
    sys.exit()

fas_dir = sys.argv[1]
out_dir = sys.argv[2]

#put files into a list
fas_list = []
for fas in os.listdir(fas_dir):
    if fas.endswith("fasta") or fas.endswith("fas"):
        fas_list.append(fas)
#print(fas_list)

#Need to process this list now
cmd_list = []
counter = 0
for fas_file in fas_list:
    counter += 1
    #fas_file = fas_list[i] + fas_dir  # file.fa + /path/to/file -> file.fa/path/to/file/
    #print(fas_dir + fas_file)
    #So now you've told python which files you want to process.
    out_name = fas_file.replace('.fas', '.zorro.output')
    out_file = out_dir + out_name

    #Where to put output files _^

    zorro_cmd = ('/data/bop17lhy/probmask/trunk/src/zorro'
                 ' {} > {}').format(fas_dir + fas_file, out_file)
    cmd_list.append(zorro_cmd)

    print(fas_dir+fas_file, out_file, sep='\t')

    #print(zorro_cmd)


# for i in range(0, len(cmd_list), 10):
#     bin_cmds = cmd_list[i:i+100]
#     bin_outs = out_dir + 'jobs' + str(i) + str(i+100)
#     #Change below to qsub when you want to submit.
#     q_sub(bin_cmds, out=bin_outs)
