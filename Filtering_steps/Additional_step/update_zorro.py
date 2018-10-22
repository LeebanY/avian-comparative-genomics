import os
import sys
import re

#locations:
#fas_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/PRANK/'
zorro_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/ZORRO/'
gblocks_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/GBLOCKS/'
out_dir = '/data/bop17lhy/sequences/PIPELINE/Filters/updated_zorro/'


zorro_list= []
for file in os.listdir(zorro_dir):
    if file.endswith('.output'):
        zorro_list.append(file)

gblocks_list = []
for g in os.listdir(gblocks_dir):
    if g.endswith('fas-gb.txt'):
        gblocks_list.append(g)

# x_list=[]
# #print(gblocks_list)
# for x in zorro_list:
#     x = '/data/bop17lhy/sequences/PIPELINE/Filters/GBLOCKS/'+x+'.cds.best.fas.best.fas-gb.txt'
#     x_list.append(x)
#
# #(gblocks_list)
# dict = {}

gblocks_list.sort()
zorro_list.sort()

for i in range(0, len(zorro_list)):
    zorro_file = zorro_dir + zorro_list[i]
    gblocks_file = gblocks_dir + gblocks_list[i]




    gblocks_contents = str(open(gblocks_file).read())
    #print(gblocks_contents)
    gblocks_contents = gblocks_contents.split('Gblocks')[-1]
    gblocks_contents = gblocks_contents.split('\n')[0]
   # print(gblocks_contents)
   #  M_str = re.search('#', gblocks_contents)
   #  #print(M_str)
   #  #m_beg = M_str.start()
   #  M_count = gblocks_contents.count('#')
   #  remaining_length = m_beg + M_count
   #  m_end = len(gblocks_contents) - remaining_length





    zorro_contents = str(open(zorro_file).read())
    zorro_contents = zorro_contents.split('\n')
    #print(zorro_contents)
    #print(zorro_contents)
    zorro_length = len(zorro_contents)

    updated_zorro = []

    for x in range(0, len(zorro_contents)):
        zor = zorro_contents[x]
        gblocks = gblocks_contents[x]
        #print(zor, gblocks)

        if gblocks == '#':
            updated_zorro.append(zor)

    #updated_zorro = str(updated_zorro)
    #print(updated_zorro)

    id = zorro_file.split('/')[-1]
    id = id+'.updated'
    #print(updated_zorro)


    outwrite = open(out_dir + id, 'w')
    for y in updated_zorro:
        #print(y)
        outwrite.write(y + '\n')

    outwrite.close()



