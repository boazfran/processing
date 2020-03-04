
AssignGenes.py igblast -s 1.fasta -b ~/share/igblast --organism human --loci ig --format blast
MakeDb.py igblast -i 1_igblast.fmt7 -s 1.fasta -r ~/share/germlines/imgt/human/vdj IMGT_Human_IGHV.fasta IMGT_Human_IGHD.fasta IMGT_Human_IGHJ.fasta
DefineClones.py -d 1_igblast_db-pass.tab