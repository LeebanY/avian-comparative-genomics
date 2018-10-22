from __future__ import print_function
import os
from itertools import islice
import sys
from Bio import SeqIO


phylip_files = '/data/bop17lhy/sequences/prepped_files/'
fas_dir = '/data/bop17lhy/sequences/ali/'
outsets = '/data/bop17lhy/sequences/PIPELINE/ali/'

#print(fas_list)


for file in os.listdir(phylip_files):
    #print(file)
    if not file.endswith(".phylip"): continue
    contents = open(phylip_files+file).read()
    #span=2
    new_contents = contents.split()
    #print(new_contents)
    species_list = []
    for x in new_contents:
        if len(x) < 60 and len(x) > 10 :
            species_list.append(x)
           # print(species_list)


        # if file doesn't begin with fas - skip in

        # read
    id = file.replace('phylip', 'fas')
    #print(id)

    fasta = SeqIO.index(fas_dir + id, "fasta")

        # filter and write
    outwrite = open(outsets + id, 'w')
    #print(id)
    for f in fasta:
        if f in species_list:
            outwrite.write('>' + f + '\n' + str(fasta[f].seq) + '\n')
    outwrite.close()



