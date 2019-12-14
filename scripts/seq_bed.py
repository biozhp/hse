import os
import re
from Bio import SeqIO
import argparse
from itertools import combinations
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-i', type=str)
args = parser.parse_args()
inf = args.i
dict_file = [r for r in open("./scripts/temp/temp1.txt","r")]
inf_2 = [r for r in open("./scripts/temp/temp4.txt","r")]
ouf_2 = open("./scripts/temp/temp5.txt","w")
dict_1 = {}
for line1 in dict_file:
    li1 = line1.strip().split()
    dict_1[li1[0]] =li1[1]
for line2 in inf_2:
    li2 = line2.strip().split()
    dict_li20 = str(li2[1])
    if dict_li20 in dict_1:
        ouf_2.write("%s\t%s\t%s\t%s\t%s\t%s\n" %(li2[0],dict_li20,li2[2],li2[3],li2[4],dict_1[dict_li20]))
ouf_2.close()
os.system("cat ./scripts/temp/temp5.txt ./scripts/header2.txt > ./scripts/temp/temp6.txt")
inf3 = [r for r in open("./scripts/temp/temp6.txt", "r")]
ouf3 = open("./scripts/temp/temp7.txt", "w")
oldgeneid = "1"
oldnum = int("1")
oldcdsid = "1"
old_chr = "1"
old_pos_tiqu = "1"
old_zhengfu = "1"
for line5 in inf3:
    li5 = line5.strip().split()
    if li5[0] == oldgeneid:
        oldgeneid = li5[0]
        if int(li5[5]) > oldnum:
            oldnum = int(li5[5])
            oldcdsid = li5[1]
            old_chr = li5[2]
            old_pos_tiqu = li5[3]
            old_zhengfu = li5[4]
    else:
        ouf3.write("%s\t%s\t%s\t%s\t%s\n" % (oldgeneid, oldcdsid, old_chr,old_pos_tiqu,old_zhengfu))
        oldnum = int(li5[5])
        oldcdsid = li5[1]
        old_chr = li5[2]
        old_pos_tiqu = li5[3]
        old_zhengfu = li5[4]
        oldgeneid = li5[0]
ouf3.close()
inf1 = [r for r in open("./scripts/temp/temp7.txt", "r")]
infasta = [r for r in open(inf, "r")]
outf1 = open("./scripts/temp/temp9.txt", "w")
dict_fasta = {}
for fl in infasta:
    fl = fl.strip().split()
    dict_fasta[fl[0]] = fl[1]
for line3 in inf1:
    line3 = line3.replace("\n","")
    li1 = line3.strip().split()
    num2 = int(li1[3])
    if li1[4] == "-":
        numb = num2 + 2001
        numb1 = num2 + 1
        if int(numb) > int(dict_fasta[li1[2]]):
            numb = int(dict_fasta[li1[2]]) + 1
            outf1.write('%s\t%s%s%s%s%s%s%s\n' % (li1[1], li1[2], "&", numb1, "&", numb, "&", li1[4]))
        else:
            outf1.write('%s\t%s%s%s%s%s%s%s\n' % (li1[1], li1[2], "&", numb1, "&", numb, "&", li1[4]))
    else:
        numb = num2 - 2000
        numb1 = num2
        if numb1 > 1:
            if numb < 0:
                numb = 1
                outf1.write('%s\t%s%s%s%s%s%s%s\n' % (li1[1], li1[2], "&", numb, "&", numb1, "&", li1[4]))
            else:
                outf1.write('%s\t%s%s%s%s%s%s%s\n' % (li1[1], li1[2], "&", numb, "&", numb1, "&", li1[4]))
outf1.close()
inff = [r for r in open("./scripts/temp/temp9.txt", "r")]
outf = open("./scripts/temp/seq.bed", "w")
for line in inff:
    li = re.split("&|\t", line)
    qishi = int(li[2]) - 1
    if qishi < 0:
    	qishi = 0
    zhongzhi = int(li[3]) - 1
    if zhongzhi < 0:
    	zhongzhi = 0
    outf.write("%s\t%s\t%s\t%s\t%s\t%s" % (li[1], qishi, zhongzhi,li[0], "S", li[4]))
outf.close()
