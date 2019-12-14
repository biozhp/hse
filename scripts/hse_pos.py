import re
inf = [r for r in open("./scripts/temp/hse5.txt","r")]
ouf = open("./scripts/temp/hse6.txt","w")
for line in inf:
    line = line.replace("\n","")
    li = re.split("\t|\.",line)
    pos1 = 2001 - int(li[3])
    pos2 = 2001 - int(li[2])
    ouf.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li[0],pos1,pos2,li[4],li[5],li[6],li[7]))
