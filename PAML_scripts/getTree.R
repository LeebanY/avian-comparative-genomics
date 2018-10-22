rm(list=ls())

library(ape)

#setwd("/Users/leebanyusuf/Desktop/Labbook/Beak_shape_morphology/Extract_rates/")

#lookup <- read.csv("Species_names_lookup_table_V2.csv", strings=F)
new_spp<- read.csv("newlist.csv", strings=F) 



##Need to read in list of species names that I have.


raw.hack <- read.nexus("Data/RAW/Genus.nexus.Hackett.tre")
#raw.hack <- read.nexus("Data/RAW/Genus.nexus.Prum.tre")

traits <- c("MULTIVAR") #Edited to include only multivar

errors <- c()

# Match to tree names


fspp <- new_spp$nature_paper_match

  
  # You want to get a data frame which is identical to lookup, but only has the species you are interested in.
  # Then, just keep the nature_paper_match column. So bascially the fspp but just your species names.
  
  # Subset main (time) trees:
timetree.hack <- drop.tip(raw.hack, setdiff(raw.hack$tip.label, fspp))
#timetree.prum <- drop.tip(raw.hack, setdiff(raw.prum$tip.label, fspp))
  

    
# Hackett - You can just run all of the hackett stuff (plus a comparison with a new scaled tree that you read in)
scaled <- read.tree(paste0("Data/HACKETT/", traits, "/", traits, "_MeanScaledTree.tre"))
scaled <- drop.tip(scaled, setdiff(scaled$tip.label, fspp))
rates <- scaled
rates$edge.length <- scaled$edge.length / timetree.hack$edge.length # calculate rates as: amount of change along branch / length of branch (i.e time). This avoids problems associated with simply subsetting rates trees (i.e. rates must be averaged when a sister species is pruned away)
rates$tip.label <- new_spp$taxon_name[match(rates$tip.label, new_spp$nature_paper_match)]
write.tree(rates, "MeanRateTree_NaturePaper.tre")
    
tr <- read.tree("MeanRateTree_NaturePaper.tre")

#print(tr)
unrooted_tr <- unroot(tr)
#print(unrooted_tr)
write.tree(unrooted_tr,"MeanRateTree_NaturePaper_unroot.tre")


#errors <- data.frame(errors, stringsAsFactors = F)
#errors
#colnames(errors) <- c("gene","excluded")

#write.csv(errors, "Outputs/Nature_paper_beak_rates/Excluded_gene_tree_tips.csv", row.names = F)


# ======================================== #

