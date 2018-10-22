from __future__ import print_function
import os
import sys

otherdir = '/data/bop17lhy/sequences/second_trimmed_files/'
indir = '/data/bop17lhy/sequences/prepped_files/'
phylip_list = []
for phylip in os.listdir(indir):
     if phylip.endswith(".phylip"):
        phylip_list.append(phylip)


otherlist =[]
for x in os.listdir(otherdir):
    if x.endswith(".phylip"):
        otherlist.append(x)


#print(phylip_list)

for files in otherlist:
    if files in phylip_list:continue

    os.rename('/data/bop17lhy/sequences/second_trimmed_files/{}'.format(files),
              '/data/bop17lhy/sequences/output_prep/{}'.format(files))

