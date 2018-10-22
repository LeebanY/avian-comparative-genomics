from qsub import q_sub
import os
import sys

#locations

# protein_alignment = '/data/bop17lhy/sequences/FINAL_PIPELINE/Filters/TEST_filtered_prot/'
# codon_alignment = '/data/bop17lhy/sequences/FINAL_PIPELINE/Filters/TEST_filtered_cds/'
# out_dir = '/data/bop17lhy/sequences/FINAL_PIPELINE/Filters/PAL2NAL/'

protein_alignment = '/data/bop17lhy/sequences/PIPELINE/Filters/filtered_ali/'
codon_alignment = '/data/bop17lhy/sequences/PIPELINE/Filters/filtered_cds/'
out_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/PAL2NAL/'

cds_list = []
fas_list = []

for fas in os.listdir(protein_alignment):
    if fas.endswith("fas"):
        fas_list.append(fas)


for cds in os.listdir(codon_alignment):
    if cds.endswith('cds'):
        cds_list.append(cds)

#dictionary = dict(zip(fas_list, cds_list))

cmd_list = []

for i in range(0, len(fas_list)):

    fas = fas_list[i]
    cds = cds_list[i]

    fas_file = '/data/bop17lhy/sequences/PIPELINE/Filters/filtered_ali/' + fas
    cds_file = '/data/bop17lhy/sequences/PIPELINE/Filters/filtered_cds/' + cds

    out_name = fas.replace('fas', 'paml')

    out_file = out_dir + out_name


    pal2nal_cmd = ('/data/bop17lhy/pal2nal.v14/pal2nal.pl'
                   ' {} {} -nogap '
                   '-output paml > {}').format(fas_file, cds_file, out_file)
    #print pal2nal_cmd

    cmd_list.append(pal2nal_cmd)


for i in range(0, len(cmd_list), 100):
    bin_cmds = cmd_list[i:i+100]
    bin_outs = out_dir + 'jobs' + str(i) + str(i+100)
    #Change below to qsub when you want to submit.
    q_sub(bin_cmds, out=bin_outs)




# RUN PAL2NAL
#os.system('perl pal2nal.pl tmpfiles/ali.fa tmpfiles/nuc.fa -nogap -output paml > tmpfiles/ali.paml')






#Running this on python 3









# REMOVE FAKE
# info=open('tmpfiles/ali.paml').read()
# info=info.split('FAKE_X')[0]
# info=info.replace(str(no_specs+1),str(no_specs),1)
# outwrite=open('output/final_'+str(k)+'.paml','w')
# outwrite.write(info)
# outwrite.close()