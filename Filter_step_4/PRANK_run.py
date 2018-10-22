from qsub import q_sub
import os
import sys

fas_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/Filter_ds/'
fas_list = []
out_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/PRANK/'
#Put files into fas_list
for fas in os.listdir(fas_dir):
    if fas.endswith(".fas"):
        fas_list.append(fas)



cmd_list = []

#For files in range of the fas list: process files
for i in range(0, len(fas_list)):
    fas_file = fas_dir + fas_list[i]

    out_name = fas_file.replace('.fas', '.fas').split('/')[-1]
    out_file = out_dir + out_name

    prank_cmd = ('/data/bop17lhy/prank-msa/src/prank -d={} '
                   '-o={}').format(fas_file, out_file)

    cmd_list.append(prank_cmd)

    #print(fas_file, out_file, sep='\t')

    #out_dir = '/data/bop17lhy/sequences/gblocks_files_new/'

for i in range(0, len(cmd_list), 100):
    bin_cmds = cmd_list[i:i+100]
    bin_outs = out_dir + 'jobs' + str(i) + str(i+100)

    q_sub(bin_cmds, out=bin_outs)