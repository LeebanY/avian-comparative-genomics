import os
import sys
from Bio import SeqIO

#locations

# protein_alignment = '/data/bop17lhy/sequences/filters_attempt2/filtered_prot/'
# codon_alignment = '/data/bop17lhy/sequences/filters_attempt2/filter5_cds/'
# outsets = '/data/bop17lhy/sequences/filters_attempt2/filtered_cds/'

protein_alignment = '/data/bop17lhy/sequences/PIPELINE/Filters/PRANK/'
codon_alignment = '/data/bop17lhy/sequences/PIPELINE/cds/'
outsets = '/data/bop17lhy/sequences/PIPELINE/Filters/part_filtered_cds/'

#Put fasta files in list.
fas_list = []
for fas in os.listdir(protein_alignment):
    if fas.endswith(".fas"):
        fas_list.append(fas)

#Loop through cds files
for cds in os.listdir(codon_alignment):
    codons = SeqIO.index(codon_alignment + cds, 'fasta') #Read cds files
    fas = cds + '.best.fas'+'.best.fas' #added the last bit because of a mistake in test run - remove in proper run
    if fas not in os.listdir(protein_alignment):continue
    fasta = SeqIO.index(protein_alignment + fas, 'fasta')


    outwrite = open(outsets + cds, 'w')
    for key in codons:
        #print(key)
        if key not in fasta:continue

        outwrite.write('>' + key + '\n' + str(codons[key].seq) + '\n')

    outwrite.close()
















