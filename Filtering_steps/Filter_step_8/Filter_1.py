from qsub import q_print
import os
import sys
import shutil

reference_files = '/data/bop17lhy/masters_scripts/removing_small_species.txt'
#reference_files = '/data/bop17lhy/sequences/filters_attempt2/filter6/first_filter.txt'
#reference_files = '/data/bop17lhy/sequences/TEST_RUN_3/phylip_Files/first_filter.txt'
protein_alignments= '/data/bop17lhy/sequences/PIPELINE/Filters/CODE/alignments/'

#protein_alignments = '/data/bop17lhy/sequences/ali_for_filters/'
#paml_alignments = '/data/bop17lhy/sequences/filters_attempt2/filter6/'
#out_dir = '/data/bop17lhy/sequences/filters_attempt2/filter1'
#out_dir = '/data/bop17lhy/sequences/filters_attempt2/final_alignment_set'
out_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/CODE/new_alignments/'


proteins = os.listdir(protein_alignments)


ref_contents = open(reference_files).readlines()
passed_fastas = []
for lines in ref_contents:
    ref_contents = lines.split('/')
    new_ref = ref_contents[-1].replace('\n', '')
    #print(new_ref)
    # new_ref = new_ref.rsplit('\n')[0]
    passed_fastas.append(new_ref)



#print(passed_fastas)


#Be careful with this it might mess everything up.
for fasta in passed_fastas:
    #print(fasta)
    # id = fasta.replace('.phylip', '.fas')
    # print(id)
    try:
        os.rename('/data/bop17lhy/sequences/PIPELINE/Filters/CODE/alignments/{}'.format(fasta),
                  '/data/bop17lhy/sequences/PIPELINE/Filters/CODE/new_alignments/{}'.format(fasta))

#     # if this raise the below error
    except OSError:
        continue





