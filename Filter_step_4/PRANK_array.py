import subprocess
import sys


list_file = sys.argv[1]
sge_id = int(sys.argv[2])

# this line is ugly, opens our tst file listing pairs of input and output files
# then selects the line corrosponding to the SGE_TASK_ID (-1 because python zero based)
run_files = open(list_file).readlines()[sge_id-1].rstrip().split()
in_file, out_file = run_files[0], run_files[1]

cmd = '/data/bop17lhy/prank-msa/src/prank -d={} -o={}'.format(in_file, out_file)
subprocess.call(cmd, shell=True)
