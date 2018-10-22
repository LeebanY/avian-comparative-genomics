import os
import sys
from Bio import SeqIO

reference_files = '/data/bop17lhy/masters_scripts/ds_filter.txt'  # dn filter > dnds > ds

# ortholog_sets = '/data/bop17lhy/sequences/filters_attempt2/filter_4_dn/' #file with current orthologs
ortholog_sets = '/data/bop17lhy/sequences/PIPELINE/Filters/Filter_species_length/'

# outsets='/data/bop17lhy/sequences/filters_attempt2/filter_4_dnds/'
outsets = '/data/bop17lhy/sequences/PIPELINE/Filters/Filter_ds/'
# where they're going to be outwritten too.


bad_species = {}

for line in open(reference_files).readlines():
    new_lines = line.split('\n')[0]
    #print(new_lines)
    spec = new_lines.split()[1]
    #print(spec)
    filename = str(new_lines.split()[0])
    filename = filename.replace(',', '')
    filename = filename.replace("'", '')
    # .split('/')[-1] # just the file name
    filename += '.cds.best.fas'
    #print(filename)
    if filename not in bad_species: bad_species[filename] = []
    bad_species[filename].append(spec)

#print(bad_species)

for fas in os.listdir(ortholog_sets):
    # if file doesn't begin with fas - skip it
    if not fas.endswith(".fas"): continue

    # read
    fasta = SeqIO.index(ortholog_sets + fas, "fasta")

    # filter and write
    outwrite = open(outsets + fas, 'w')

    for f in fasta:
        if fas in bad_species and f in bad_species[fas]:continue
        outwrite.write('>' + f + '\n' + str(fasta[f].seq) + '\n')
    outwrite.close()
