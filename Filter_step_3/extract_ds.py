from __future__ import print_function
import os
import sys
import numpy as np
import re
#from qsub import q_sub



# check for questionable species based on pairwise alignment (mod3)

indir = '/data/bop17lhy/sequences/PIPELINE/pairwise_output/' #directory: sequences/check_pairwise_dnds_output

#out_dir = '/data/bop17lhy/sequences/filters/jobs_out_dir/'

alle=os.listdir(indir)

alle.sort()
#headers for csv
#print("dn/ds", "mean", "min", 'max')

reference_file = '/data/bop17lhy/masters_scripts/ds_ref_list.txt'
reference_contents = open(reference_file).readlines()


gg_tg_ds={}


for re in reference_contents:
	ru=re.split(',')
	gg_tg_ds[ru[0]]=float(ru[1])



#print(gg_tg_ds)

for a in alle[:]:
    # filenames = open(indir + a).readline()
    # filenames = filenames.split('/')
    # filenames = filenames[-1]
    # filenames = filenames.split('.')
    # filenames = filenames[0]+'.cds.best_dnds.phy'


    info = open(indir + a).read()
    if len(info) < 5000:
        continue
    get_filename = info.split('Model: several dN/dS ratios for branches for branches')[0]
    #print(get_filename)
    filename = get_filename.split('/')
    filename = filename[-1]
    filename = filename.split('.')
    filename = filename[0]+'.cds.best_dnds.phy'
    #print(filename)


    # check ns
    liste = {}
    numsp = int(info.split('ls =')[0].split('\nns =')[-1])  # gets number of spp from file







    info = info.split('pairwise comparison, codon frequencies: F3x4.')[-1]
    dN = []
    dS = []
    dN_dS = []
    #dict_1 = {}

    for k in info.split('\n\n\n')[1:]:
        # Put pairwise of species into two different list (species 1 and species 2)
       #  split = k.split()
       #  #print(split)
       #  split_ds = split[-1]
       #  split_ds = split_ds.replace('=', '')
       #
       #
       #
       #  # =============================================
       #  dict_1 = {}
       #  ds_score = []
       #
       #
       #
       # # print(split_ds)
       #
       #
       #  if split[1] == '(Gallus_gallus)' and split[4] == '(Taeniopygia_guttata)':
       #      print(filename, split_ds, sep=',')




            #print(ds_score)

                # if filename not in dict_1: dict_1[filename]= []
                # dict_1[filename].append(score)
                #
                # print(filename)

        # =============================================
        #
        # for a in gg_tg_ds:
        #     if 'rna3266.cds.best_dnds.phy' == a :
        #         print(a)
        #         break



        #=============================================
        spec1 = k.split(' ')[1].strip()[1:-1]
        spec2 = k.split(' ')[4].strip()[1:-5]


        # print(spec1, spec2)
        #
        # Not particular sure what is going here: if x is not in species 1 -> put into species 1 list(same for spec2).
        # THIS IS TO INITIALIZE THE LIST
        if spec1 not in liste:
            liste[spec1] = []
        if spec2 not in liste:
            liste[spec2] = []


        #print(spec1, spec2)

        # Error here with species - Doesn't recognise a particular species.
        # Append lists with dn/ds, ds and dn.

        # print(liste)


        #liste[spec1].append(float(k.split('dN/dS=')[1].split('dN')[0]))
        liste[spec1].append(float(k.split('dS =')[1].split('\n')[0]))
        #liste[spec1].append(float(k.split('dN =')[1].split('dS')[0]))
        #print(liste)

        #liste[spec2].append(float(k.split('dN/dS=')[1].split('dN')[0]))
        liste[spec2].append(float(k.split('dS =')[1].split('\n')[0]))
        # liste[spec2].append(float(k.split('dN =')[1].split('dS')[0]))
        # print(liste)
        #
        #
        # print(liste)
        #
        # val_mean = np.mean(liste[spec1]) + np.mean(liste[spec2])
        # val_std = np.std(liste[spec1]) + np.std(liste[spec2])
        #
        # mean_spec1 = np.mean(liste[spec1])
        # mean_spec2 = np.mean(liste[spec2])
        # mean_sp = mean_spec1 + mean_spec2
        # min_sp1 = np.min(liste[spec1])
        # min_sp2 = np.min(liste[spec2])
        # min_sp = min_sp1 + min_sp2
        # max_sp1 = np.max(liste[spec1])
        # max_sp2 = np.max(liste[spec2])
        # maxsp = max_sp1 + max_sp2
        # print(val, mean_sp, min_sp, maxsp)
        #
        # print(val)
        # for l in liste:
        #     for val in val_mean:
        #         if val > 2.0:
        #             print(val)
        #             break
        #
        # median_set = list(set(np.median(liste[l])))



    for l in liste:
        curprint=False
        if np.median(liste[l]) > 5: curprint=True
        # DOUBLE CHECK WHETHER YOU REALLY HAVE ALL PAIRWISE DS!!!!
        if a in gg_tg_ds:
			if np.median(liste[l]) >= gg_tg_ds[a]*5: curprint=True
        if curprint: print(a.split('.')[0], l,  np.median(liste[l]))

