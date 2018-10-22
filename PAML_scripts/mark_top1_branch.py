import os, sys

# files for which trees 2b created
indir='trees/'
alle=os.listdir(indir)

# 
for a in alle[:]:

	info=open(indir+a).read()

	vals=[]
	for k in info.split(':')[1:]:
		number=k.split(')')[0].split(',')[0]
		vals.append([float(number),number])
	vals.sort()

	# mark top branch
	for v in vals[:-3]:
		info=info.replace(':'+v[1],'')

	info=info.replace(':'+vals[-3][1],'')
	info=info.replace(':'+vals[-2][1],'')
	info=info.replace(':'+vals[-1][1],' #1')

	outwrite=open('top1tree/'+a,'w')
	outwrite.write(info)
	outwrite.close()

