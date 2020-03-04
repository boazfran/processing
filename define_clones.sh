
for dir in GMC FV IB ; do
	AssignGenes.py igblast -s $dir/full.fasta -b ~/share/igblast --organism human --loci ig --format blast --outdir $dir;
	MakeDb.py igblast -i $dir/full_igblast.fmt7 -s $dir/full.fasta -r ~/share/germlines/imgt/human/vdj IMGT_Human_IGHV.fasta IMGT_Human_IGHD.fasta IMGT_Human_IGHJ.fasta --outdir $dir;
	DefineClones.py -d $dir/full_igblast_db-pass.tab --outdir $dir;
done
