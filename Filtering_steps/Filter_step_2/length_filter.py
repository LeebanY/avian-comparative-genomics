import pysam
import os
import numpy as np
# inputs
#fas_dir = '/data/bop17lhy/sequences/filters_attempt2/filter2/'
#fas_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/Filter_species_no/'

fas_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/Filter_species_length/'


ref_spp = "Gallus_gallus"

# get fasta list
fas_list = []
for fas in os.listdir(fas_dir):
    if fas.endswith(".fas"):
       fas_list.append(fas_dir + fas)



#print(fas_list)
# print header
print('filename', 'sequence_length', sep=',')
# process each fasta file in turn
for x in fas_list:
    #if x == '/data/bop17lhy/sequences/PIPELINE/Filters/PRANK/rna20362.cds.best.fas.best.fas': continue
    fasta = pysam.FastaFile(x)
    spp_in_file = fasta.references
    alignment_length = fasta.lengths[0]
    if x == fas_dir+'rna17629.cds.best.fas':
        print(x, spp_in_file)
    # if alignment_length >= 1500:
    #     print(x, alignment_length)
    if ref_spp not in fasta:continue

    # get the length of reference sequence to compare against
    ref_length = alignment_length - fasta.fetch(ref_spp).count('-')
    spp_length =[]
    # loop through all species in the fasta file
    for species in spp_in_file:

        # skip reference species
        if species == ref_spp:
            continue

        # fetch sequence for current species from fasta file
        spp_seq = fasta.fetch(species)

        # count number of gaps in sequence
        spp_length = alignment_length - spp_seq.count('-')


    # if spp_length >= 1500:
    #     continue
    #
    # if spp_length <= 50:
    #     continue
    # if spp_length > 56 :
    #     print(x, spp_length, sep=',')

    #piped into good_lengths_filter.txt
