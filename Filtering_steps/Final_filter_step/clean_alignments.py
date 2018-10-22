import os, sys

indir = '/data/bop17lhy/sequences/TEST_RUN_3/Filter_stages/Filter_AFT_PAL2NAL/'
outdir = '/data/bop17lhy/sequences/TEST_RUN_3/Filter_stages/final_alignment/'

alle = os.listdir(indir)
# REMOVE FAKE
for a in alle:
    info = open(indir + a).read()
    no_specs = -1

    for i in info.split('\n'):
        if i.find('_') > -1: no_specs += 1
    info = info.split('FAKE_X')[0]
    deletespecs = no_specs
    # print info
    if info.find('Haliaeetus_albicilla') > -1 and info.find('Haliaeetus_leucocephalus') > -1:
        # print "FOUND"

        info1 = info.split('Haliaeetus_leucocephalus')[0]
        info2 = info.split('Haliaeetus_leucocephalus')[1].split('_', 1)[1]
        infoM = info.split('Haliaeetus_leucocephalus')[1].split('_')[0].rsplit('\n', 1)[-1]

        # print info1
        # print infoM
        # print info2
        info = info1 + infoM + '_' + info2
        deletespecs -= 1
    #	info=info.replace(str(no_specs+1),str(no_specs-1),1)
    # else:
    if info.find('Falco_cherrug') > -1 and info.find('Falco_peregrinus') > -1:
        # print "FOUND"

        info1 = info.split('Falco_peregrinus')[0]
        info2 = info.split('Falco_peregrinus')[1].split('_', 1)[1]
        infoM = info.split('Falco_peregrinus')[1].split('_')[0].rsplit('\n', 1)[-1]

        # print info1
        # print infoM
        # print info2
        info = info1 + infoM + '_' + info2
        deletespecs -= 1

    if info.find('Corvus_brachyrhynchos') > -1 and info.find('Corvus_cornix_cornix') > -1:
        info1 = info.split('Corvus_cornix_cornix')[0]
        info2 = info.split('Corvus_cornix_cornix')[1].split('_', 1)[1]
        infoM = info.split('Corvus_cornix_cornix')[1].split('_')[0].rsplit('\n', 1)[-1]

        info = info1 + infoM + '_' + info2
        deletespecs -= 1

    info = info.replace(str(no_specs + 1), str(deletespecs), 1)
    outwrite = open(outdir + a, 'w')
    outwrite.write(info)
    outwrite.close()