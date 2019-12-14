#!/bin/bash
## Usages: sh ./run_pipeline.sh cds.fa gene.gff3 genome_chr_length.txt genome.fa output_file
## By Peng Zhao
## Email: pengzhao@nwafu.edu.cn
## Need to install bedtools (https://github.com/arq5x/bedtools2/releases) and add to environment variables before running
## Need to install biopython (https://biopython.org/wiki/Download) and add to environment variables before running
cds=$1
gff=$2
length=$3
genome=$4
ouf=$5
python ./scripts/max_cds_length.py -i ${cds} -g ${gff} && \
python ./scripts/seq_bed.py -i ${length} && \
bedtools getfasta -name -s -fi ${genome} -bed ./scripts/temp/seq.bed -fo ./scripts/temp/promoter.fa && \
python ./scripts/hse_call.py && \
python ./scripts/hse_result.py && \
python ./scripts/hse_mismatch.py && \
sort -t $'\t' -k1,1 -k2n,2 -k5n,5 ./scripts/temp/hse4.txt > ./scripts/temp/hse5.txt && \
python ./scripts/hse_pos.py && \
mv ./scripts/temp/hse6.txt ${ouf} && \
rm ./scripts/temp/*
rm ./*.finish
