import os, sys

# files for which trees 2b created
indir='alignments_clean/'
alle=os.listdir(indir)
# possible species
info=open('Species_names_lookup_table_V2Joe.csv','rU').readlines() 

treemap={}
# Start process for each file
for a in alle[:]:
	# get species in the alignment
	species=[]
	for x in open(indir+a).readlines():
		specnow=x.rstrip().split('_')
		specnow2=x.rstrip()
		#if x.find('_')>-1: species.append(specnow[0]+'_'+specnow[1])
		if x.find('_')>-1: species.append(specnow2)
	outwrite=open('newlist.csv','w')
	outwrite.write(info[0])
	counter=0
#
	# print a, counter, len(species)
	# print species
#
	# extract species from list
	for i in info[1:]:
		#print i.split(',')[5]
		if i.split(',')[4] in species:
			species.remove(i.split(',')[4])
			outwrite.write(i)
			counter+=1
 	outwrite.close()
	#print counter
#
#
#
# 	# rerun script
	os.system('Rscript getTree.R')

	# move output

	os.system('mv MeanRateTree_NaturePaper_unroot.tre trees/'+a+'.tre')
