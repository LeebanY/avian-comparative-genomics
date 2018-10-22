import os, sys

sdir='scripts/'
for s in os.listdir(sdir):
	print
	os.system('sh '+sdir+s)
	
	# Use appropriate qsub here
	





