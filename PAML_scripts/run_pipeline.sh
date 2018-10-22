rm -R running/*
rm -R scripts/*
#rm -R trees/*
rm top1tree/*
rm top2tree/*
rm top3tree/*
#python clean_alignments.py
#python create_trees.py
python mark_top1_branch.py
python mark_top2_branch.py
python mark_top3_branch.py
python mark_binned_branch.py
python prepare_codeml.py
#python runCODEML50.py
