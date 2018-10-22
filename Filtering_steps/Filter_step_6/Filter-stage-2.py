import os
import sys
#locations


#reference_files = '/data/bop17lhy/masters_scripts/bad_vals_zorro_PIPE3.txt'
reference_files = '/data/bop17lhy/masters_scripts/removing_stop_codons_faslist.txt'

# reference_files = '/data/bop17lhy/masters_scripts/bad_vals_zorro_rd2.txt'
# protein_alignments = '/data/bop17lhy/sequences/filters_attempt2/filter1'


#processing reference files from txt file

ref_contents = open(reference_files).readlines()
passed_fastas = []
for line in ref_contents:
    split_ref = line.split('/')
    new_contents = split_ref[7]
    #print(new_contents)
    new_ref = new_contents.rsplit('\n')[0]
    passed_fastas.append(new_ref)
    print(new_ref)



#print(passed_fastas)


for fasta in passed_fastas:

    # tries to run file moving
    try:
        os.rename('/data/bop17lhy/sequences/TEST_RUN_3/Filter_stages/filtered_prot/'.format(fasta),
                  '/data/bop17lhy/sequences/TEST_RUN_3/Filter_stages/final_alignment/'.format(fasta))
        # os.rename('/data/bop17lhy/sequences/filters/filter1.1/{}.fai'.format(fasta),
        #           '/data/bop17lhy/sequences/filters/filter1.2/{}.fai'.format(fasta))

    # if this raise the below error
    except FileNotFoundError:
        continue