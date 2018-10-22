import os
import sys
from Bio import SeqIO
from group_files import group_files

#Locations
gblocks = '/data/bop17lhy/sequences/PIPELINE/Filters/GBLOCKS/'
zorro = '/data/bop17lhy/sequences/PIPELINE/Filters/ZORRO/'
orthologs = '/data/bop17lhy/sequences/PIPELINE/Filters/PRANK/'
codons = '/data/bop17lhy/sequences/PIPELINE/Filters/part_filtered_cds/'
outsets_protein= '/data/bop17lhy/sequences/PIPELINE/Filters/filtered_cds/'
outsets_cds = '/data/bop17lhy/sequences/PIPELINE/Filters/filtered_prot/'


#Storing everything in
gblocks_contents = os.listdir(gblocks)
zorro_contents = os.listdir(zorro)
protein_alignments = os.listdir(outsets_protein)
codon_alignments = os.listdir(codons)
rna_files = group_files(gblocks, zorro, orthologs, codons)


#Check the contents work: they do.
#print(codon_alignments)



for files in rna_files.values():
    try:
        gblocks_file = files[1]
        zorro_file = files[2]
        fasta_file = files[0]
        codon_file = files[3]
        #print(fasta_file)

        info = open(gblocks_file).read()
        #print info
        info = info.split('Gblocks  ')[1].split('\n\n')[0]
        info = info.replace(' ', '')
        info = info.replace('.', '-')
        info = info.replace('#', 'M')
        #print 'start'
        #print info
        #print 'stop'

        #print fasta_file

        #Zorro - amend fake sequence based on ZORRO.
        info2 = ''
        for x in open(zorro_file).readlines():
            if float(x) > 9:
                info2 += 'M'

            else:
                info2 += '-'







        #Create empty vars for fake prot and cds seqs.
        # merging
        outprot = ''
        outdna = ''
        for x in range(len(info)):
            if info[x] == 'M' and info2[x]=='M':
                outprot += 'M'
                outdna += 'AUG'
            else:
                outprot += '-'
                outdna += '-'





        #print outprot

        fasta = SeqIO.index(fasta_file, "fasta")
        #print fasta_file
        #Outwrite fake seq to protein
        outwrite = open(outsets_protein + fasta_file.rsplit('/', 1)[-1], 'w')


        # add new sequence to old contents
        fas_contents = open(fasta_file).read()
        fas_contents += '>FAKE_X\n' + outprot + '\n'

        # write to new file
        outwrite.write(fas_contents)
        outwrite.close()

        #
        #cds_fasta = SeqIO.index(codon_file, "fasta")
        outwrite_cds = open(outsets_cds + codon_file.rsplit('/', 1)[-1], 'w')

        codon_contents = open(codon_file).read()
        codon_contents += '>FAKE_X\n' + outdna + '\n'
        outwrite_cds.write(codon_contents)

        outwrite_cds.close()

    except IndexError:
        continue

#
#
#
#
#
