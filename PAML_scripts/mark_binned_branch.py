import os, sys
from scipy.cluster import vq
import numpy as np

# files for which trees 2b created
indir = 'trees/'
alle = os.listdir(indir)

#
for a in alle[:]:

		info = open(indir + a).read()

		vals = []  # numeric+strng
		valsn = []  # numeric only
		for k in info.split(':')[1:]:
			number = k.split(')')[0].split(',')[0]
			vals.append([float(number), number])
			valsn.append(float(number))

		# CLUSTER ME, 8 bins - maybe empty
		centroids = vq.kmeans2(np.array(valsn), 8)

		maps = {}
		sets = list(set(centroids[-1]))
		sets.sort()
		for k in range(len(sets)):
			maps[sets[k]] = k

		# mark branches
		for v in range(len(vals)):
			info = info.replace(':' + vals[v][1], ' #' + str(maps[centroids[-1][v]]))

		outwrite = open('binned_tree/' + a, 'w')
		outwrite.write(info)
		outwrite.close()
