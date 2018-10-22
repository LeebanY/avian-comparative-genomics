#from qsub import q_print
import os
import sys

#n_spp = sys.argv[1] #Just input a number you want to match the species list in every file with. Example "57".
#Use >= 20 - all species with 20 or more species to maximise number of orthologs for analysis.

#Locations
#trimmed_files = '/data/bop17lhy/sequences/PIPELINE_THREE/Filters/TEST/phylip_files/'
#trimmed_files = '/data/bop17lhy/sequences/filters_attempt2/filter6/'
#trimmed_files ='/data/bop17lhy/sequences/filters_attempt2/final_alignment_set_copy/alignments/'
trimmed_files = '/data/bop17lhy/sequences/PIPELINE/Filters/CODE/alignments/'

# make file list
trimmed_files_list = []
for phy in os.listdir(trimmed_files):
    if phy.endswith("paml"):
        trimmed_files_list.append(trimmed_files + phy)

#print(trimmed_files_list)

liste = []
# make list of ok files
ok_files = open(trimmed_files + 'first_filter.txt', 'w')
for phylip_files in trimmed_files_list:
    contents = open(phylip_files).readline()
    if contents == ' ': continue
    if contents == '': continue
    #print(contents)
    # new_contents = contents.split()
    # new_contents = new_contents[-1]
    #print(new_contents)
#
#
    #print(phylip_files, int(contents[1:4]))
    if int(contents[1:4]) >= int(20):
       print(phylip_files)










