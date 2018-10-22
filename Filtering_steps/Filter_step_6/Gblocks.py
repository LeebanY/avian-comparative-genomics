from qsub import q_sub
import os
import sys

fas_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/PRANK/'
fas_list = []
#Put files into fas_list
for fas in os.listdir(fas_dir):
    if fas.endswith(".fas"):
        fas_list.append(fas)



cmd_list = []

#For files in range of the fas list: process files
for i in range(0, len(fas_list)):
    fas_file = fas_dir + fas_list[i]

    gblocks_cmd = ('/data/bop17lhy/sequences/gblocks_files/Gblocks {}'
                   ' -k=y -n=y -p=t -v=32000').format(fas_file)

    cmd_list.append(gblocks_cmd)

    out_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/GBLOCKS/'

for i in range(0, len(cmd_list), 100):
    bin_cmds = cmd_list[i:i+100]
    bin_outs = out_dir + 'jobs' + str(i) + str(i+100)

    q_sub(bin_cmds, out=bin_outs)




