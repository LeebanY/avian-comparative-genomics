import os


def group_files(gb_dir, zor_dir, fa_dir, cds_dir):

    """
    loops through three directories and groups files from each by rna
    :param gb_dir: str
    :param zor_dir: str
    :param fa_dir: str
    :param cds_dir: str
    :return: dict
    """

    grouped_files = {}

    for fasta in os.listdir(fa_dir):

        # skip non fasta files
        if not fasta.endswith('.fas'):
            continue

        seq_id = fasta.split('.')[0]

        grouped_files[seq_id] = [fa_dir + fasta]

    for gb in os.listdir(gb_dir):

        seq_id = gb.split('.')[0]

        # if rna id is not in dictionary skip (ie no fasta file for that rna)
        if seq_id not in grouped_files.keys():
            continue

        grouped_files[seq_id].append(gb_dir + gb)

    for zor in os.listdir(zor_dir):

        seq_id = zor.split('.')[0]


        # if rna id is not in dictionary skip (ie no fasta file for that rna)
        if seq_id not in grouped_files.keys():
            continue

        grouped_files[seq_id].append(zor_dir + zor)

    for cds in os.listdir(cds_dir):

        seq_id = cds.split('.')[0]

        # if rna id is not in dictionary skip (ie no fasta file for that rna)
        if seq_id not in grouped_files.keys():
            continue

        grouped_files[seq_id].append(cds_dir + cds)

    return grouped_files

# # debug
gblocks = '/data/bop17lhy/sequences/PIPELINE/Filters/GBLOCKS/'
zorro = '/data/bop17lhy/sequences/PIPELINE/Filters/ZORRO/'
orthologs = '/data/bop17lhy/sequences/PIPELINE/Filters/PRANK/'
codons = '/data/bop17lhy/sequences/PIPELINE/Filters/part_filtered_cds/'

rna_files = group_files(gblocks, zorro, orthologs, codons)

# for x in rna_files.items():
#       print(x)