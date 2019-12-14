import re
import os
from Bio import SeqIO
import argparse
from itertools import combinations
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-i', type=str)
parser.add_argument('-g', type=str)
args = parser.parse_args()
inf = args.i
inf_gff = args.g
import re
from Bio import SeqIO
records = [r for r in SeqIO.parse(inf, "fasta")]
put_file = open("./scripts/temp/temp1.txt", "w")
for line in records:
    changdu = len(line.seq)
    atg = line.seq[:3]
    if atg == "ATG":
        put_file.write("%s\t%s\n" % (line.id, changdu))
put_file.close()
infile = [r for r in open(inf_gff, "r")]
outfile = open("./scripts/temp/temp2.txt", "w")
for b in infile:
    b = re.split(";|\t|ID=|Parent=|Name=", b)
    if len(b) > 3:
        if b[2] == "gene":
            geneid = str(b[9])
        elif b[2] == "CDS":
            cdsid = str(b[9]).replace("\n","")
            outfile.write("%s\t%s\t%s%s%s%s%s%s%s\n" % (geneid, cdsid, b[0],"&",b[3],"&",b[4],"&",b[6]))
outfile.close()
os.system("cat ./scripts/temp/temp2.txt ./scripts/header.txt > ./scripts/temp/temp3.txt")
inf2 = [r for r in open("./scripts/temp/temp3.txt","r")]
ouf2 = open("./scripts/temp/temp4.txt","w")
old_cds_id = "1"
old_pos ="1"
gene_id = "1"
chr_id = "1"
zhengfu = "1"
for line3 in inf2:
    li3 = re.split("\t|&|\n",line3)
    if li3[1] == old_cds_id:
        gene_id = li3[0]
        old_cds_id = li3[1]
        chr_id = li3[2]
        zhengfu = li3[5]
        if li3[5] == "-":
            pos = int(li3[4])
            if pos > old_pos:
                old_pos = int(li3[4])
        if li3[5] == "+":
            pos = int(li3[3])
            if pos < old_pos:
                old_pos = int(li3[3])
    else:
        ouf2.write("%s\t%s\t%s\t%s\t%s\n" % (gene_id,old_cds_id,chr_id,old_pos,zhengfu))
        gene_id = li3[0]
        old_cds_id = li3[1]
        chr_id = li3[2]
        zhengfu = li3[5]
        if li3[5] == "-":
            old_pos = int(li3[4])
        elif li3[5] == "+":
            old_pos = int(li3[3])
ouf2.close()
