import os
import sys
import numpy as np



# check for questionable species based on pairwise alignment (mod3)

indir = '/data/bop17lhy/sequences/PIPELINE/pairwise_output/' #directory: sequences/check_pairwise_dnds_output
#out_dir = '/data/bop17lhy/sequences/filters/jobs_out_dir/'

alle=os.listdir(indir)

alle.sort()
#headers for csv
#print("dn/ds", "mean", "min", 'max')



for a in alle[:]:
    info = open(indir + a).read()
    if len(info) < 5000:
        continue
    # if a == 'rna11152.cds.best_dnds.phy':continue
    # check ns
    liste = {}
    numsp = int(info.split('ls =')[0].split('\nns =')[-1])  # gets number of spp from file
    info = info.split('pairwise comparison, codon frequencies: F3x4.')[-1]
    dN = []
    dS = []
    dN_dS = []


    for k in info.split('\n\n\n')[1:]:
        # print(a)
        # print(float(k.split('dN/dS=')[1].split('dN')[0]))



        # Put pairwise of species into two different list (species 1 and species 2)
        spec1 = k.split(' ')[1].strip()[1:-1]
        spec2 = k.split(' ')[4].strip()[1:-5]

        #print(spec1, spec2)


        # Not particular sure what is going here: if x is not in species 1 -> put into species 1 list(same for spec2).
        if spec1 not in liste:
            liste[spec1] = []
        if spec2 not in liste:
            liste[spec2] = []



        #
        #
        # #print(spec1, spec2)
        #
        # # Error here with species - Doesn't recognise a particular species.
        # # Append lists with dn/ds, ds and dn.
        #
        # # print(liste)
        #
        #
         #liste[spec1].append(float(k.split('dN/dS=')[1].split('dN')[0]))
    #     #liste[spec1].append(float(k.split('dS =')[1].split('\n')[0]))
        liste[spec1].append(float(k.split('dN =')[1].split('dS')[0]))
    #     #
    #     #
    #     #
    #     # #print(liste)
    #     #
        #liste[spec2].append(float(k.split('dN/dS=')[1].split('dN')[0]))
    #     # #liste[spec2].append(float(k.split('dS =')[1].split('\n')[0]))
        liste[spec2].append(float(k.split('dN =')[1].split('dS')[0]))
    #     #
    #
    #
    #
    #     #print(liste)
    #
    #     # val_mean = np.mean(liste[spec1]) + np.mean(liste[spec2])
    #     # val_std = np.std(liste[spec1]) + np.std(liste[spec2])
    #     #
    #     # mean_spec1 = np.mean(liste[spec1])
    #     # mean_spec2 = np.mean(liste[spec2])
    #     # mean_sp = mean_spec1 + mean_spec2
    #     # min_sp1 = np.min(liste[spec1])
    #     # min_sp2 = np.min(liste[spec2])
    #     # min_sp = min_sp1 + min_sp2
    #     # max_sp1 = np.max(liste[spec1])
    #     # max_sp2 = np.max(liste[spec2])
    #     # maxsp = max_sp1 + max_sp2
    #     # print(val, mean_sp, min_sp, maxsp)
    #
    #     # print(val)
    #     # for l in liste:
    #     #     for val in val_mean:
    #     #         if val > 2.0:
    #     #             print(val)
    #     #             break
    #
    #     #median_set = list(set(np.median(liste[l])))
    #
    #
    # #
    for l in liste:

    #
    #
         if np.median(liste[l]) > 2.0:
             print(a.split('.')[0], l,  np.median(liste[l]))