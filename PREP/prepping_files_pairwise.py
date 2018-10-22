from __future__ import print_function
import os, sys
import numpy as np

indir = '/data/bop17lhy/sequences/output_prep/'
outdir = '/data/bop17lhy/sequences/prepped_files/'

alle = os.listdir(indir)

def nongapable(seqsdict, length, glen):
    total = np.zeros(length)
    for s in seqsdict:
        cur = []
        for k in seqsdict[s]:
            if k in ['?', '-', 'N', 'n']:
                cur.append(1)
            else:
                cur.append(0)
        total += np.array(cur)
    return list(total).count(0) / float(glen)


for a in alle:
    # READ IN FILES
    rows = open(indir + a).readlines()
    seqs = {}
    for r in rows[2:]:
        info = r.split(' ')
        if info[0].rstrip() == '': continue
        seqs[info[0]] = info[-1].rstrip()

    # missing info
    m_info = []
    for i in seqs:
        missing = seqs[i].count('-') + seqs[i].count('N')
        liste = seqs[i].split('-')
        # print missing
        pieces = len(liste) - liste.count('')
        # print missing, pieces
        m_info.append([missing, i, pieces, seqs[i]])
    le = len(seqs[i])
    m_info.sort()
    m_info = m_info[::-1]
    print(a)
    # Filter out seqeunces with more than 0.2 missing, too many gaps and overall alignment length
    if 'Gallus_gallus' not in seqs:continue
    gallus_len = len(seqs['Gallus_gallus'].upper()) - seqs['Gallus_gallus'].count('-') - seqs['Gallus_gallus'].upper().count('N')
    for m in m_info:
        # skip for gallus gallus
        if m[1] == 'Gallus_gallus':
            continue
        # if more than 20%
        # if float(m[0])/gallus_len>0.2: seqs.pop(m[1])
        # elif m[2]>6:  seqs.pop(m[1])
        elif nongapable(seqs, le, gallus_len) < 0.8:
            seqs.pop(m[1])
    # Filter more sequences if
    #
    ausgabe = open(outdir + a, 'w')
    ausgabe.write('  ' + str(len(seqs)) + '  ' + str(le) + '\n')
    for s in seqs:
        ausgabe.write(s + '\n' + seqs[s].upper() + '\n')
    ausgabe.close()


