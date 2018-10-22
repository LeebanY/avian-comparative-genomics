import os, sys, shutil

# Dependencies
# the tree file (e.g. top1tree)
# cleaned alignment file

# INPUT FILES
alignments = 'alignments_clean/'
allfiles= os.listdir(alignments)
trees1='top1tree/'
trees2='top2tree/'
trees3='top3tree/'
trees4='binned_tree/'
trees5='trees/'

for ali in allfiles:
	treefile=ali+'.tre'
	rundir='running/'+ali.split('.')[0]+'/'
	# create folder for running
	os.system('mkdir '+rundir)

    # Copy files (ctls, tree and alignment)
    # This is for hotspots! - here we use a branch model instead of branch site model
    # SO THIS IS ONLY BRANCH TESTS
	
	# STEP1: copy the alignment
	os.system('cp '+alignments+ali+' '+rundir+'inpaml.txt')
	
	# STEP2: copy the trees
	os.system('cp '+trees1+treefile+' '+rundir+'inpaml.tre')
	os.system('cp '+trees2+treefile+' '+rundir+'inpaml_2.tre')
	os.system('cp '+trees3+treefile+' '+rundir+'inpaml_3.tre')
	os.system('cp '+trees4+treefile+' '+rundir+'inpaml_4.tre')
	os.system('cp '+trees5+treefile+' '+rundir+'inpaml_5.tre')	
	
	# STEP3: copy the ctl files
	os.system('cp codeml_templateTop1.ctl '+rundir+'BranchTop1.ctl')
	os.system('cp codeml_templateTop2.ctl '+rundir+'BranchTop2.ctl')
	os.system('cp codeml_templateTop3.ctl '+rundir+'BranchTop3.ctl')
	os.system('cp codeml_templateBins.ctl '+rundir+'BranchBinned.ctl')
	# THIS IS THE ALTERNATIVE MODEL, COMMON TO ALL COMPARISONS
	os.system('cp codeml_templateNoBins.ctl '+rundir+'BranchNoBin.ctl')



rundirs=os.listdir('running/')

counter=0
for r in rundirs:
	if counter%50==0:
		if counter!=0:
			outwrite.close()
			#os.system('sh scripts/batch'+str(counter-50)+'.sh') 
			outwrite=open('scripts/batch'+str(counter)+'.sh','w')
		else: outwrite=open('scripts/batch'+str(counter)+'.sh','w')
	outwrite.write('cd running/'+r+'\n') 
	outwrite.write('../../codeml BranchBinned.ctl\n') 
	outwrite.write('../../codeml BranchNoBin.ctl\n')	
	outwrite.write('../../codeml BranchTop1.ctl\n') 
	outwrite.write('../../codeml BranchTop2.ctl\n') 
	outwrite.write('../../codeml BranchTop3.ctl\n') 
	outwrite.write('cd ../..\n')
	counter+=1
outwrite.close()


	





