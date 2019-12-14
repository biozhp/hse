import re
inf1 = [r for r in open("./scripts/hse_template.txt","r")]
inf2 = [r for r in open("./scripts/temp/hse2.txt","r")]
ouf = open("./scripts/temp/hse3.txt","w")
dict_hse = {}
for line1 in inf1:
    li1 = line1.strip().split()
    dict_hse[li1[0]] = li1[1]
for line2 in inf2:
    li2 = line2.strip().split()
    if li2[4] in dict_hse.keys():
        sample_seq = dict_hse[li2[4]]
        if len(li2[3]) == 15:
            record1 = str(li2[3])
            sub_record1 = record1[1:4]
            sub_record2 = record1[6:9]
            sub_record3 = record1[11:14]
            sub_seq = sub_record1 + sub_record2 + sub_record3
            cutseq1 = sub_seq[:1]
            cutseq2 = sub_seq[1:2]
            cutseq3 = sub_seq[2:3]
            cutseq4 = sub_seq[3:4]
            cutseq5 = sub_seq[4:5]
            cutseq6 = sub_seq[5:6]
            cutseq7 = sub_seq[6:7]
            cutseq8 = sub_seq[7:8]
            cutseq9 = sub_seq[8:]
            samcut1 = sample_seq[:1]
            samcut2 = sample_seq[1:2]
            samcut3 = sample_seq[2:3]
            samcut4 = sample_seq[3:4]
            samcut5 = sample_seq[4:5]
            samcut6 = sample_seq[5:6]
            samcut7 = sample_seq[6:7]
            samcut8 = sample_seq[7:8]
            samcut9 = sample_seq[8:]
            data = []
            data_num = []
            if cutseq1 != samcut1:
                cut1 = cutseq1 + samcut1
                cutnum1 = "1:2"
                data.append(cut1)
                data_num.append(cutnum1)
            if cutseq2 != samcut2:
                cut2 = cutseq2 + samcut2
                cutnum2 = "1:3"
                data.append(cut2)
                data_num.append(cutnum2)
            if cutseq3 != samcut3:
                cut3 = cutseq3 + samcut3
                cutnum3 = "1:4"
                data.append(cut3)
                data_num.append(cutnum3)
            if cutseq4 != samcut4:
                cut4 = cutseq4 + samcut4
                cutnum4 = "2:2"
                data.append(cut4)
                data_num.append(cutnum4)
            if cutseq5 != samcut5:
                cut5 = cutseq5 + samcut5
                cutnum5 = "2:3"
                data.append(cut5)
                data_num.append(cutnum5)
            if cutseq6 != samcut6:
                cut6 = cutseq6 + samcut6
                cutnum6 = "2:4"
                data.append(cut6)
                data_num.append(cutnum6)
            if cutseq7 != samcut7:
                cut7 = cutseq7 + samcut7
                cutnum7 = "3:2"
                data.append(cut7)
                data_num.append(cutnum7)
            if cutseq8 != samcut8:
                cut8 = cutseq8 + samcut8
                cutnum8 = "3:3"
                data.append(cut8)
                data_num.append(cutnum8)
            if cutseq9 != samcut9:
                cut9 = cutseq9 + samcut9
                cutnum9 = "3:4"
                data.append(cut9)
                data_num.append(cutnum9)
            ouf.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li2[0], li2[1], li2[2], li2[3], li2[4], data, data_num))
        if len(li2[3]) == 20:
            record1 = str(li2[3])
            sub_record1 = record1[1:4]
            sub_record2 = record1[6:9]
            sub_record3 = record1[11:14]
            sub_record4 = record1[16:19]
            sub_seq = sub_record1 + sub_record2 + sub_record3 + sub_record4
            cutseq1 = sub_seq[:1]
            cutseq2 = sub_seq[1:2]
            cutseq3 = sub_seq[2:3]
            cutseq4 = sub_seq[3:4]
            cutseq5 = sub_seq[4:5]
            cutseq6 = sub_seq[5:6]
            cutseq7 = sub_seq[6:7]
            cutseq8 = sub_seq[7:8]
            cutseq9 = sub_seq[8:9]
            cutseq10 = sub_seq[9:10]
            cutseq11 = sub_seq[10:11]
            cutseq12 = sub_seq[11:]
            samcut1 = sample_seq[:1]
            samcut2 = sample_seq[1:2]
            samcut3 = sample_seq[2:3]
            samcut4 = sample_seq[3:4]
            samcut5 = sample_seq[4:5]
            samcut6 = sample_seq[5:6]
            samcut7 = sample_seq[6:7]
            samcut8 = sample_seq[7:8]
            samcut9 = sample_seq[8:9]
            samcut10 = sample_seq[9:10]
            samcut11 = sample_seq[10:11]
            samcut12 = sample_seq[11:]
            data = []
            data_num = []
            if cutseq1 != samcut1:
                cut1 = cutseq1 + samcut1
                cutnum1 = "1:2"
                data.append(cut1)
                data_num.append(cutnum1)
            if cutseq2 != samcut2:
                cut2 = cutseq2 + samcut2
                cutnum2 = "1:3"
                data.append(cut2)
                data_num.append(cutnum2)
            if cutseq3 != samcut3:
                cut3 = cutseq3 + samcut3
                cutnum3 = "1:4"
                data.append(cut3)
                data_num.append(cutnum3)
            if cutseq4 != samcut4:
                cut4 = cutseq4 + samcut4
                cutnum4 = "2:2"
                data.append(cut4)
                data_num.append(cutnum4)
            if cutseq5 != samcut5:
                cut5 = cutseq5 + samcut5
                cutnum5 = "2:3"
                data.append(cut5)
                data_num.append(cutnum5)
            if cutseq6 != samcut6:
                cut6 = cutseq6 + samcut6
                cutnum6 = "2:4"
                data.append(cut6)
                data_num.append(cutnum6)
            if cutseq7 != samcut7:
                cut7 = cutseq7 + samcut7
                cutnum7 = "3:2"
                data.append(cut7)
                data_num.append(cutnum7)
            if cutseq8 != samcut8:
                cut8 = cutseq8 + samcut8
                cutnum8 = "3:3"
                data.append(cut8)
                data_num.append(cutnum8)
            if cutseq9 != samcut9:
                cut9 = cutseq9 + samcut9
                cutnum9 = "3:4"
                data.append(cut9)
                data_num.append(cutnum9)
            if cutseq10 != samcut10:
                cut10 = cutseq10 + samcut10
                cutnum10 = "4:2"
                data.append(cut10)
                data_num.append(cutnum10)
            if cutseq11 != samcut11:
                cut11 = cutseq11 + samcut11
                cutnum11 = "4:3"
                data.append(cut11)
                data_num.append(cutnum11)
            if cutseq12 != samcut12:
                cut12 = cutseq12 + samcut12
                cutnum12 = "4:4"
                data.append(cut12)
                data_num.append(cutnum12)
            ouf.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li2[0], li2[1], li2[2], li2[3], li2[4], data, data_num))
        if len(li2[3]) == 25:
            record1 = str(li2[3])
            sub_record1 = record1[1:4]
            sub_record2 = record1[6:9]
            sub_record3 = record1[11:14]
            sub_record4 = record1[16:19]
            sub_record5 = record1[21:24]
            sub_seq = sub_record1 + sub_record2 + sub_record3 + sub_record4 + sub_record5
            cutseq1 = sub_seq[:1]
            cutseq2 = sub_seq[1:2]
            cutseq3 = sub_seq[2:3]
            cutseq4 = sub_seq[3:4]
            cutseq5 = sub_seq[4:5]
            cutseq6 = sub_seq[5:6]
            cutseq7 = sub_seq[6:7]
            cutseq8 = sub_seq[7:8]
            cutseq9 = sub_seq[8:9]
            cutseq10 = sub_seq[9:10]
            cutseq11 = sub_seq[10:11]
            cutseq12 = sub_seq[11:12]
            cutseq13 = sub_seq[12:13]
            cutseq14 = sub_seq[13:14]
            cutseq15 = sub_seq[14:]
            samcut1 = sample_seq[:1]
            samcut2 = sample_seq[1:2]
            samcut3 = sample_seq[2:3]
            samcut4 = sample_seq[3:4]
            samcut5 = sample_seq[4:5]
            samcut6 = sample_seq[5:6]
            samcut7 = sample_seq[6:7]
            samcut8 = sample_seq[7:8]
            samcut9 = sample_seq[8:9]
            samcut10 = sample_seq[9:10]
            samcut11 = sample_seq[10:11]
            samcut12 = sample_seq[11:12]
            samcut13 = sample_seq[12:13]
            samcut14 = sample_seq[13:14]
            samcut15 = sample_seq[14:]
            data = []
            data_num = []
            if cutseq1 != samcut1:
                cut1 = cutseq1 + samcut1
                cutnum1 = "1:2"
                data.append(cut1)
                data_num.append(cutnum1)
            if cutseq2 != samcut2:
                cut2 = cutseq2 + samcut2
                cutnum2 = "1:3"
                data.append(cut2)
                data_num.append(cutnum2)
            if cutseq3 != samcut3:
                cut3 = cutseq3 + samcut3
                cutnum3 = "1:4"
                data.append(cut3)
                data_num.append(cutnum3)
            if cutseq4 != samcut4:
                cut4 = cutseq4 + samcut4
                cutnum4 = "2:2"
                data.append(cut4)
                data_num.append(cutnum4)
            if cutseq5 != samcut5:
                cut5 = cutseq5 + samcut5
                cutnum5 = "2:3"
                data.append(cut5)
                data_num.append(cutnum5)
            if cutseq6 != samcut6:
                cut6 = cutseq6 + samcut6
                cutnum6 = "2:4"
                data.append(cut6)
                data_num.append(cutnum6)
            if cutseq7 != samcut7:
                cut7 = cutseq7 + samcut7
                cutnum7 = "3:2"
                data.append(cut7)
                data_num.append(cutnum7)
            if cutseq8 != samcut8:
                cut8 = cutseq8 + samcut8
                cutnum8 = "3:3"
                data.append(cut8)
                data_num.append(cutnum8)
            if cutseq9 != samcut9:
                cut9 = cutseq9 + samcut9
                cutnum9 = "3:4"
                data.append(cut9)
                data_num.append(cutnum9)
            if cutseq10 != samcut10:
                cut10 = cutseq10 + samcut10
                cutnum10 = "4:2"
                data.append(cut10)
                data_num.append(cutnum10)
            if cutseq11 != samcut11:
                cut11 = cutseq11 + samcut11
                cutnum11 = "4:3"
                data.append(cut11)
                data_num.append(cutnum11)
            if cutseq12 != samcut12:
                cut12 = cutseq12 + samcut12
                cutnum12 = "4:4"
                data.append(cut12)
                data_num.append(cutnum12)
            if cutseq13 != samcut13:
                cut13 = cutseq13 + samcut13
                cutnum13 = "5:2"
                data.append(cut13)
                data_num.append(cutnum13)
            if cutseq14 != samcut14:
                cut14 = cutseq14 + samcut14
                cutnum14 = "5:3"
                data.append(cut14)
                data_num.append(cutnum14)
            if cutseq15 != samcut15:
                cut15 = cutseq15 + samcut15
                cutnum15 = "5:4"
                data.append(cut15)
                data_num.append(cutnum15)
            ouf.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li2[0], li2[1], li2[2], li2[3], li2[4], data, data_num))
        if len(li2[3]) == 30:
            record1 = str(li2[3])
            sub_record1 = record1[1:4]
            sub_record2 = record1[6:9]
            sub_record3 = record1[11:14]
            sub_record4 = record1[16:19]
            sub_record5 = record1[21:24]
            sub_record6 = record1[26:29]
            sub_seq = sub_record1 + sub_record2 + sub_record3 + sub_record4+ sub_record5+ sub_record6
            cutseq1 = sub_seq[:1]
            cutseq2 = sub_seq[1:2]
            cutseq3 = sub_seq[2:3]
            cutseq4 = sub_seq[3:4]
            cutseq5 = sub_seq[4:5]
            cutseq6 = sub_seq[5:6]
            cutseq7 = sub_seq[6:7]
            cutseq8 = sub_seq[7:8]
            cutseq9 = sub_seq[8:9]
            cutseq10 = sub_seq[9:10]
            cutseq11 = sub_seq[10:11]
            cutseq12 = sub_seq[11:12]
            cutseq13 = sub_seq[12:13]
            cutseq14 = sub_seq[13:14]
            cutseq15 = sub_seq[14:15]
            cutseq16 = sub_seq[15:16]
            cutseq17 = sub_seq[16:17]
            cutseq18 = sub_seq[17:]
            samcut1 = sample_seq[:1]
            samcut2 = sample_seq[1:2]
            samcut3 = sample_seq[2:3]
            samcut4 = sample_seq[3:4]
            samcut5 = sample_seq[4:5]
            samcut6 = sample_seq[5:6]
            samcut7 = sample_seq[6:7]
            samcut8 = sample_seq[7:8]
            samcut9 = sample_seq[8:9]
            samcut10 = sample_seq[9:10]
            samcut11 = sample_seq[10:11]
            samcut12 = sample_seq[11:12]
            samcut13 = sample_seq[12:13]
            samcut14 = sample_seq[13:14]
            samcut15 = sample_seq[14:15]
            samcut16 = sample_seq[15:16]
            samcut17 = sample_seq[16:17]
            samcut18 = sample_seq[17:]
            data = []
            data_num = []
            if cutseq1 != samcut1:
                cut1 = cutseq1 + samcut1
                cutnum1 = "1:2"
                data.append(cut1)
                data_num.append(cutnum1)
            if cutseq2 != samcut2:
                cut2 = cutseq2 + samcut2
                cutnum2 = "1:3"
                data.append(cut2)
                data_num.append(cutnum2)
            if cutseq3 != samcut3:
                cut3 = cutseq3 + samcut3
                cutnum3 = "1:4"
                data.append(cut3)
                data_num.append(cutnum3)
            if cutseq4 != samcut4:
                cut4 = cutseq4 + samcut4
                cutnum4 = "2:2"
                data.append(cut4)
                data_num.append(cutnum4)
            if cutseq5 != samcut5:
                cut5 = cutseq5 + samcut5
                cutnum5 = "2:3"
                data.append(cut5)
                data_num.append(cutnum5)
            if cutseq6 != samcut6:
                cut6 = cutseq6 + samcut6
                cutnum6 = "2:4"
                data.append(cut6)
                data_num.append(cutnum6)
            if cutseq7 != samcut7:
                cut7 = cutseq7 + samcut7
                cutnum7 = "3:2"
                data.append(cut7)
                data_num.append(cutnum7)
            if cutseq8 != samcut8:
                cut8 = cutseq8 + samcut8
                cutnum8 = "3:3"
                data.append(cut8)
                data_num.append(cutnum8)
            if cutseq9 != samcut9:
                cut9 = cutseq9 + samcut9
                cutnum9 = "3:4"
                data.append(cut9)
                data_num.append(cutnum9)
            if cutseq10 != samcut10:
                cut10 = cutseq10 + samcut10
                cutnum10 = "4:2"
                data.append(cut10)
                data_num.append(cutnum10)
            if cutseq11 != samcut11:
                cut11 = cutseq11 + samcut11
                cutnum11 = "4:3"
                data.append(cut11)
                data_num.append(cutnum11)
            if cutseq12 != samcut12:
                cut12 = cutseq12 + samcut12
                cutnum12 = "4:4"
                data.append(cut12)
                data_num.append(cutnum12)
            if cutseq13 != samcut13:
                cut13 = cutseq13 + samcut13
                cutnum13 = "5:2"
                data.append(cut13)
                data_num.append(cutnum13)
            if cutseq14 != samcut14:
                cut14 = cutseq14 + samcut14
                cutnum14 = "5:3"
                data.append(cut14)
                data_num.append(cutnum14)
            if cutseq15 != samcut15:
                cut15 = cutseq15 + samcut15
                cutnum15 = "5:4"
                data.append(cut15)
                data_num.append(cutnum15)
            if cutseq16 != samcut16:
                cut16 = cutseq16 + samcut16
                cutnum16 = "6:2"
                data.append(cut16)
                data_num.append(cutnum16)
            if cutseq17 != samcut17:
                cut17 = cutseq17 + samcut17
                cutnum17 = "6:3"
                data.append(cut17)
                data_num.append(cutnum17)
            if cutseq18 != samcut18:
                cut18 = cutseq18 + samcut18
                cutnum18 = "6:4"
                data.append(cut18)
                data_num.append(cutnum18)
            ouf.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li2[0], li2[1], li2[2], li2[3], li2[4],data, data_num))
        if len(li2[3]) == 35:
            record1 = str(li2[3])
            sub_record1 = record1[1:4]
            sub_record2 = record1[6:9]
            sub_record3 = record1[11:14]
            sub_record4 = record1[16:19]
            sub_record5 = record1[21:24]
            sub_record6 = record1[26:29]
            sub_record7 = record1[31:34]
            sub_seq = sub_record1 + sub_record2 + sub_record3 + sub_record4 + sub_record5 + sub_record6 + sub_record7
            cutseq1 = sub_seq[:1]
            cutseq2 = sub_seq[1:2]
            cutseq3 = sub_seq[2:3]
            cutseq4 = sub_seq[3:4]
            cutseq5 = sub_seq[4:5]
            cutseq6 = sub_seq[5:6]
            cutseq7 = sub_seq[6:7]
            cutseq8 = sub_seq[7:8]
            cutseq9 = sub_seq[8:9]
            cutseq10 = sub_seq[9:10]
            cutseq11 = sub_seq[10:11]
            cutseq12 = sub_seq[11:12]
            cutseq13 = sub_seq[12:13]
            cutseq14 = sub_seq[13:14]
            cutseq15 = sub_seq[14:15]
            cutseq16 = sub_seq[15:16]
            cutseq17 = sub_seq[16:17]
            cutseq18 = sub_seq[17:18]
            cutseq19 = sub_seq[18:19]
            cutseq20 = sub_seq[19:20]
            cutseq21 = sub_seq[20:]
            samcut1 = sample_seq[:1]
            samcut2 = sample_seq[1:2]
            samcut3 = sample_seq[2:3]
            samcut4 = sample_seq[3:4]
            samcut5 = sample_seq[4:5]
            samcut6 = sample_seq[5:6]
            samcut7 = sample_seq[6:7]
            samcut8 = sample_seq[7:8]
            samcut9 = sample_seq[8:9]
            samcut10 = sample_seq[9:10]
            samcut11 = sample_seq[10:11]
            samcut12 = sample_seq[11:12]
            samcut13 = sample_seq[12:13]
            samcut14 = sample_seq[13:14]
            samcut15 = sample_seq[14:15]
            samcut16 = sample_seq[15:16]
            samcut17 = sample_seq[16:17]
            samcut18 = sample_seq[17:18]
            samcut19 = sample_seq[18:19]
            samcut20 = sample_seq[19:20]
            samcut21 = sample_seq[20:]
            data = []
            data_num = []
            if cutseq1 != samcut1:
                cut1 = cutseq1 + samcut1
                cutnum1 = "1:2"
                data.append(cut1)
                data_num.append(cutnum1)
            if cutseq2 != samcut2:
                cut2 = cutseq2 + samcut2
                cutnum2 = "1:3"
                data.append(cut2)
                data_num.append(cutnum2)
            if cutseq3 != samcut3:
                cut3 = cutseq3 + samcut3
                cutnum3 = "1:4"
                data.append(cut3)
                data_num.append(cutnum3)
            if cutseq4 != samcut4:
                cut4 = cutseq4 + samcut4
                cutnum4 = "2:2"
                data.append(cut4)
                data_num.append(cutnum4)
            if cutseq5 != samcut5:
                cut5 = cutseq5 + samcut5
                cutnum5 = "2:3"
                data.append(cut5)
                data_num.append(cutnum5)
            if cutseq6 != samcut6:
                cut6 = cutseq6 + samcut6
                cutnum6 = "2:4"
                data.append(cut6)
                data_num.append(cutnum6)
            if cutseq7 != samcut7:
                cut7 = cutseq7 + samcut7
                cutnum7 = "3:2"
                data.append(cut7)
                data_num.append(cutnum7)
            if cutseq8 != samcut8:
                cut8 = cutseq8 + samcut8
                cutnum8 = "3:3"
                data.append(cut8)
                data_num.append(cutnum8)
            if cutseq9 != samcut9:
                cut9 = cutseq9 + samcut9
                cutnum9 = "3:4"
                data.append(cut9)
                data_num.append(cutnum9)
            if cutseq10 != samcut10:
                cut10 = cutseq10 + samcut10
                cutnum10 = "4:2"
                data.append(cut10)
                data_num.append(cutnum10)
            if cutseq11 != samcut11:
                cut11 = cutseq11 + samcut11
                cutnum11 = "4:3"
                data.append(cut11)
                data_num.append(cutnum11)
            if cutseq12 != samcut12:
                cut12 = cutseq12 + samcut12
                cutnum12 = "4:4"
                data.append(cut12)
                data_num.append(cutnum12)
            if cutseq13 != samcut13:
                cut13 = cutseq13 + samcut13
                cutnum13 = "5:2"
                data.append(cut13)
                data_num.append(cutnum13)
            if cutseq14 != samcut14:
                cut14 = cutseq14 + samcut14
                cutnum14 = "5:3"
                data.append(cut14)
                data_num.append(cutnum14)
            if cutseq15 != samcut15:
                cut15 = cutseq15 + samcut15
                cutnum15 = "5:4"
                data.append(cut15)
                data_num.append(cutnum15)
            if cutseq16 != samcut16:
                cut16 = cutseq16 + samcut16
                cutnum16 = "6:2"
                data.append(cut16)
                data_num.append(cutnum16)
            if cutseq17 != samcut17:
                cut17 = cutseq17 + samcut17
                cutnum17 = "6:3"
                data.append(cut17)
                data_num.append(cutnum17)
            if cutseq18 != samcut18:
                cut18 = cutseq18 + samcut18
                cutnum18 = "6:4"
                data.append(cut18)
                data_num.append(cutnum18)
            if cutseq19 != samcut19:
                cut19 = cutseq19 + samcut19
                cutnum19 = "7:2"
                data.append(cut19)
                data_num.append(cutnum19)
            if cutseq20 != samcut20:
                cut20 = cutseq20 + samcut20
                cutnum20 = "7:3"
                data.append(cut20)
                data_num.append(cutnum20)
            if cutseq21 != samcut21:
                cut21 = cutseq21 + samcut21
                cutnum21 = "7:4"
                data.append(cut21)
                data_num.append(cutnum21)
            ouf.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li2[0], li2[1], li2[2], li2[3], li2[4],data, data_num))
        if len(li2[3]) == 40:
            record1 = str(li2[3])
            sub_record1 = record1[1:4]
            sub_record2 = record1[6:9]
            sub_record3 = record1[11:14]
            sub_record4 = record1[16:19]
            sub_record5 = record1[21:24]
            sub_record6 = record1[26:29]
            sub_record7 = record1[31:34]
            sub_record8 = record1[36:39]
            sub_seq = sub_record1 + sub_record2 + sub_record3 + sub_record4 + sub_record5 + sub_record6 + sub_record7 + sub_record8
            cutseq1 = sub_seq[:1]
            cutseq2 = sub_seq[1:2]
            cutseq3 = sub_seq[2:3]
            cutseq4 = sub_seq[3:4]
            cutseq5 = sub_seq[4:5]
            cutseq6 = sub_seq[5:6]
            cutseq7 = sub_seq[6:7]
            cutseq8 = sub_seq[7:8]
            cutseq9 = sub_seq[8:9]
            cutseq10 = sub_seq[9:10]
            cutseq11 = sub_seq[10:11]
            cutseq12 = sub_seq[11:12]
            cutseq13 = sub_seq[12:13]
            cutseq14 = sub_seq[13:14]
            cutseq15 = sub_seq[14:15]
            cutseq16 = sub_seq[15:16]
            cutseq17 = sub_seq[16:17]
            cutseq18 = sub_seq[17:18]
            cutseq19 = sub_seq[18:19]
            cutseq20 = sub_seq[19:20]
            cutseq21 = sub_seq[20:21]
            cutseq22 = sub_seq[21:22]
            cutseq23 = sub_seq[22:23]
            cutseq24 = sub_seq[23:]
            samcut1 = sample_seq[:1]
            samcut2 = sample_seq[1:2]
            samcut3 = sample_seq[2:3]
            samcut4 = sample_seq[3:4]
            samcut5 = sample_seq[4:5]
            samcut6 = sample_seq[5:6]
            samcut7 = sample_seq[6:7]
            samcut8 = sample_seq[7:8]
            samcut9 = sample_seq[8:9]
            samcut10 = sample_seq[9:10]
            samcut11 = sample_seq[10:11]
            samcut12 = sample_seq[11:12]
            samcut13 = sample_seq[12:13]
            samcut14 = sample_seq[13:14]
            samcut15 = sample_seq[14:15]
            samcut16 = sample_seq[15:16]
            samcut17 = sample_seq[16:17]
            samcut18 = sample_seq[17:18]
            samcut19 = sample_seq[18:19]
            samcut20 = sample_seq[19:20]
            samcut21 = sample_seq[20:21]
            samcut22 = sample_seq[21:22]
            samcut23 = sample_seq[22:23]
            samcut24 = sample_seq[23:]
            data = []
            data_num = []
            if cutseq1 != samcut1:
                cut1 = cutseq1 + samcut1
                cutnum1 = "1:2"
                data.append(cut1)
                data_num.append(cutnum1)
            if cutseq2 != samcut2:
                cut2 = cutseq2 + samcut2
                cutnum2 = "1:3"
                data.append(cut2)
                data_num.append(cutnum2)
            if cutseq3 != samcut3:
                cut3 = cutseq3 + samcut3
                cutnum3 = "1:4"
                data.append(cut3)
                data_num.append(cutnum3)
            if cutseq4 != samcut4:
                cut4 = cutseq4 + samcut4
                cutnum4 = "2:2"
                data.append(cut4)
                data_num.append(cutnum4)
            if cutseq5 != samcut5:
                cut5 = cutseq5 + samcut5
                cutnum5 = "2:3"
                data.append(cut5)
                data_num.append(cutnum5)
            if cutseq6 != samcut6:
                cut6 = cutseq6 + samcut6
                cutnum6 = "2:4"
                data.append(cut6)
                data_num.append(cutnum6)
            if cutseq7 != samcut7:
                cut7 = cutseq7 + samcut7
                cutnum7 = "3:2"
                data.append(cut7)
                data_num.append(cutnum7)
            if cutseq8 != samcut8:
                cut8 = cutseq8 + samcut8
                cutnum8 = "3:3"
                data.append(cut8)
                data_num.append(cutnum8)
            if cutseq9 != samcut9:
                cut9 = cutseq9 + samcut9
                cutnum9 = "3:4"
                data.append(cut9)
                data_num.append(cutnum9)
            if cutseq10 != samcut10:
                cut10 = cutseq10 + samcut10
                cutnum10 = "4:2"
                data.append(cut10)
                data_num.append(cutnum10)
            if cutseq11 != samcut11:
                cut11 = cutseq11 + samcut11
                cutnum11 = "4:3"
                data.append(cut11)
                data_num.append(cutnum11)
            if cutseq12 != samcut12:
                cut12 = cutseq12 + samcut12
                cutnum12 = "4:4"
                data.append(cut12)
                data_num.append(cutnum12)
            if cutseq13 != samcut13:
                cut13 = cutseq13 + samcut13
                cutnum13 = "5:2"
                data.append(cut13)
                data_num.append(cutnum13)
            if cutseq14 != samcut14:
                cut14 = cutseq14 + samcut14
                cutnum14 = "5:3"
                data.append(cut14)
                data_num.append(cutnum14)
            if cutseq15 != samcut15:
                cut15 = cutseq15 + samcut15
                cutnum15 = "5:4"
                data.append(cut15)
                data_num.append(cutnum15)
            if cutseq16 != samcut16:
                cut16 = cutseq16 + samcut16
                cutnum16 = "6:2"
                data.append(cut16)
                data_num.append(cutnum16)
            if cutseq17 != samcut17:
                cut17 = cutseq17 + samcut17
                cutnum17 = "6:3"
                data.append(cut17)
                data_num.append(cutnum17)
            if cutseq18 != samcut18:
                cut18 = cutseq18 + samcut18
                cutnum18 = "6:4"
                data.append(cut18)
                data_num.append(cutnum18)
            if cutseq19 != samcut19:
                cut19 = cutseq19 + samcut19
                cutnum19 = "7:2"
                data.append(cut19)
                data_num.append(cutnum19)
            if cutseq20 != samcut20:
                cut20 = cutseq20 + samcut20
                cutnum20 = "7:3"
                data.append(cut20)
                data_num.append(cutnum20)
            if cutseq21 != samcut21:
                cut21 = cutseq21 + samcut21
                cutnum21 = "7:4"
                data.append(cut21)
                data_num.append(cutnum21)
            if cutseq22 != samcut22:
                cut22 = cutseq22 + samcut22
                cutnum22 = "8:2"
                data.append(cut22)
                data_num.append(cutnum22)
            if cutseq23 != samcut23:
                cut23 = cutseq23 + samcut23
                cutnum23 = "8:3"
                data.append(cut23)
                data_num.append(cutnum23)
            if cutseq24 != samcut24:
                cut24 = cutseq24 + samcut24
                cutnum24 = "8:4"
                data.append(cut24)
                data_num.append(cutnum24)
            ouf.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li2[0], li2[1], li2[2], li2[3], li2[4], data, data_num))
        if len(li2[3]) == 45:
            record1 = str(li2[3])
            sub_record1 = record1[1:4]
            sub_record2 = record1[6:9]
            sub_record3 = record1[11:14]
            sub_record4 = record1[16:19]
            sub_record5 = record1[21:24]
            sub_record6 = record1[26:29]
            sub_record7 = record1[31:34]
            sub_record8 = record1[36:39]
            sub_record9 = record1[41:44]
            sub_seq = sub_record1 + sub_record2 + sub_record3 + sub_record4 + sub_record5 + sub_record6 + sub_record7 + sub_record8 + sub_record9
            cutseq1 = sub_seq[:1]
            cutseq2 = sub_seq[1:2]
            cutseq3 = sub_seq[2:3]
            cutseq4 = sub_seq[3:4]
            cutseq5 = sub_seq[4:5]
            cutseq6 = sub_seq[5:6]
            cutseq7 = sub_seq[6:7]
            cutseq8 = sub_seq[7:8]
            cutseq9 = sub_seq[8:9]
            cutseq10 = sub_seq[9:10]
            cutseq11 = sub_seq[10:11]
            cutseq12 = sub_seq[11:12]
            cutseq13 = sub_seq[12:13]
            cutseq14 = sub_seq[13:14]
            cutseq15 = sub_seq[14:15]
            cutseq16 = sub_seq[15:16]
            cutseq17 = sub_seq[16:17]
            cutseq18 = sub_seq[17:18]
            cutseq19 = sub_seq[18:19]
            cutseq20 = sub_seq[19:20]
            cutseq21 = sub_seq[20:21]
            cutseq22 = sub_seq[21:22]
            cutseq23 = sub_seq[22:23]
            cutseq24 = sub_seq[23:24]
            cutseq25 = sub_seq[24:25]
            cutseq26 = sub_seq[25:26]
            cutseq27 = sub_seq[26:]
            samcut1 = sample_seq[:1]
            samcut2 = sample_seq[1:2]
            samcut3 = sample_seq[2:3]
            samcut4 = sample_seq[3:4]
            samcut5 = sample_seq[4:5]
            samcut6 = sample_seq[5:6]
            samcut7 = sample_seq[6:7]
            samcut8 = sample_seq[7:8]
            samcut9 = sample_seq[8:9]
            samcut10 = sample_seq[9:10]
            samcut11 = sample_seq[10:11]
            samcut12 = sample_seq[11:12]
            samcut13 = sample_seq[12:13]
            samcut14 = sample_seq[13:14]
            samcut15 = sample_seq[14:15]
            samcut16 = sample_seq[15:16]
            samcut17 = sample_seq[16:17]
            samcut18 = sample_seq[17:18]
            samcut19 = sample_seq[18:19]
            samcut20 = sample_seq[19:20]
            samcut21 = sample_seq[20:21]
            samcut22 = sample_seq[21:22]
            samcut23 = sample_seq[22:23]
            samcut24 = sample_seq[23:24]
            samcut25 = sample_seq[24:25]
            samcut26 = sample_seq[25:26]
            samcut27 = sample_seq[26:]
            data = []
            data_num = []
            if cutseq1 != samcut1:
                cut1 = cutseq1 + samcut1
                cutnum1 = "1:2"
                data.append(cut1)
                data_num.append(cutnum1)
            if cutseq2 != samcut2:
                cut2 = cutseq2 + samcut2
                cutnum2 = "1:3"
                data.append(cut2)
                data_num.append(cutnum2)
            if cutseq3 != samcut3:
                cut3 = cutseq3 + samcut3
                cutnum3 = "1:4"
                data.append(cut3)
                data_num.append(cutnum3)
            if cutseq4 != samcut4:
                cut4 = cutseq4 + samcut4
                cutnum4 = "2:2"
                data.append(cut4)
                data_num.append(cutnum4)
            if cutseq5 != samcut5:
                cut5 = cutseq5 + samcut5
                cutnum5 = "2:3"
                data.append(cut5)
                data_num.append(cutnum5)
            if cutseq6 != samcut6:
                cut6 = cutseq6 + samcut6
                cutnum6 = "2:4"
                data.append(cut6)
                data_num.append(cutnum6)
            if cutseq7 != samcut7:
                cut7 = cutseq7 + samcut7
                cutnum7 = "3:2"
                data.append(cut7)
                data_num.append(cutnum7)
            if cutseq8 != samcut8:
                cut8 = cutseq8 + samcut8
                cutnum8 = "3:3"
                data.append(cut8)
                data_num.append(cutnum8)
            if cutseq9 != samcut9:
                cut9 = cutseq9 + samcut9
                cutnum9 = "3:4"
                data.append(cut9)
                data_num.append(cutnum9)
            if cutseq10 != samcut10:
                cut10 = cutseq10 + samcut10
                cutnum10 = "4:2"
                data.append(cut10)
                data_num.append(cutnum10)
            if cutseq11 != samcut11:
                cut11 = cutseq11 + samcut11
                cutnum11 = "4:3"
                data.append(cut11)
                data_num.append(cutnum11)
            if cutseq12 != samcut12:
                cut12 = cutseq12 + samcut12
                cutnum12 = "4:4"
                data.append(cut12)
                data_num.append(cutnum12)
            if cutseq13 != samcut13:
                cut13 = cutseq13 + samcut13
                cutnum13 = "5:2"
                data.append(cut13)
                data_num.append(cutnum13)
            if cutseq14 != samcut14:
                cut14 = cutseq14 + samcut14
                cutnum14 = "5:3"
                data.append(cut14)
                data_num.append(cutnum14)
            if cutseq15 != samcut15:
                cut15 = cutseq15 + samcut15
                cutnum15 = "5:4"
                data.append(cut15)
                data_num.append(cutnum15)
            if cutseq16 != samcut16:
                cut16 = cutseq16 + samcut16
                cutnum16 = "6:2"
                data.append(cut16)
                data_num.append(cutnum16)
            if cutseq17 != samcut17:
                cut17 = cutseq17 + samcut17
                cutnum17 = "6:3"
                data.append(cut17)
                data_num.append(cutnum17)
            if cutseq18 != samcut18:
                cut18 = cutseq18 + samcut18
                cutnum18 = "6:4"
                data.append(cut18)
                data_num.append(cutnum18)
            if cutseq19 != samcut19:
                cut19 = cutseq19 + samcut19
                cutnum19 = "7:2"
                data.append(cut19)
                data_num.append(cutnum19)
            if cutseq20 != samcut20:
                cut20 = cutseq20 + samcut20
                cutnum20 = "7:3"
                data.append(cut20)
                data_num.append(cutnum20)
            if cutseq21 != samcut21:
                cut21 = cutseq21 + samcut21
                cutnum21 = "7:4"
                data.append(cut21)
                data_num.append(cutnum21)
            if cutseq22 != samcut22:
                cut22 = cutseq22 + samcut22
                cutnum22 = "8:2"
                data.append(cut22)
                data_num.append(cutnum22)
            if cutseq23 != samcut23:
                cut23 = cutseq23 + samcut23
                cutnum23 = "8:3"
                data.append(cut23)
                data_num.append(cutnum23)
            if cutseq24 != samcut24:
                cut24 = cutseq24 + samcut24
                cutnum24 = "8:4"
                data.append(cut24)
                data_num.append(cutnum24)
            if cutseq25 != samcut25:
                cut25 = cutseq25 + samcut25
                cutnum25 = "9:2"
                data.append(cut25)
                data_num.append(cutnum25)
            if cutseq26 != samcut26:
                cut26 = cutseq26 + samcut26
                cutnum26 = "9:3"
                data.append(cut26)
                data_num.append(cutnum26)
            if cutseq27 != samcut27:
                cut27 = cutseq27 + samcut27
                cutnum27 = "9:4"
                data.append(cut27)
                data_num.append(cutnum27)
            ouf.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li2[0], li2[1], li2[2], li2[3], li2[4],data, data_num))
        if len(li2[3]) == 50:
            record1 = str(li2[3])
            sub_record1 = record1[1:4]
            sub_record2 = record1[6:9]
            sub_record3 = record1[11:14]
            sub_record4 = record1[16:19]
            sub_record5 = record1[21:24]
            sub_record6 = record1[26:29]
            sub_record7 = record1[31:34]
            sub_record8 = record1[36:39]
            sub_record9 = record1[41:44]
            sub_record10 = record1[46:49]
            sub_seq = sub_record1 + sub_record2 + sub_record3 + sub_record4 + sub_record5 + sub_record6 + sub_record7 + sub_record8 + sub_record9 + sub_record10
            cutseq1 = sub_seq[:1]
            cutseq2 = sub_seq[1:2]
            cutseq3 = sub_seq[2:3]
            cutseq4 = sub_seq[3:4]
            cutseq5 = sub_seq[4:5]
            cutseq6 = sub_seq[5:6]
            cutseq7 = sub_seq[6:7]
            cutseq8 = sub_seq[7:8]
            cutseq9 = sub_seq[8:9]
            cutseq10 = sub_seq[9:10]
            cutseq11 = sub_seq[10:11]
            cutseq12 = sub_seq[11:12]
            cutseq13 = sub_seq[12:13]
            cutseq14 = sub_seq[13:14]
            cutseq15 = sub_seq[14:15]
            cutseq16 = sub_seq[15:16]
            cutseq17 = sub_seq[16:17]
            cutseq18 = sub_seq[17:18]
            cutseq19 = sub_seq[18:19]
            cutseq20 = sub_seq[19:20]
            cutseq21 = sub_seq[20:21]
            cutseq22 = sub_seq[21:22]
            cutseq23 = sub_seq[22:23]
            cutseq24 = sub_seq[23:24]
            cutseq25 = sub_seq[24:25]
            cutseq26 = sub_seq[25:26]
            cutseq27 = sub_seq[26:27]
            cutseq28 = sub_seq[27:28]
            cutseq29 = sub_seq[28:29]
            cutseq30 = sub_seq[29:]
            samcut1 = sample_seq[:1]
            samcut2 = sample_seq[1:2]
            samcut3 = sample_seq[2:3]
            samcut4 = sample_seq[3:4]
            samcut5 = sample_seq[4:5]
            samcut6 = sample_seq[5:6]
            samcut7 = sample_seq[6:7]
            samcut8 = sample_seq[7:8]
            samcut9 = sample_seq[8:9]
            samcut10 = sample_seq[9:10]
            samcut11 = sample_seq[10:11]
            samcut12 = sample_seq[11:12]
            samcut13 = sample_seq[12:13]
            samcut14 = sample_seq[13:14]
            samcut15 = sample_seq[14:15]
            samcut16 = sample_seq[15:16]
            samcut17 = sample_seq[16:17]
            samcut18 = sample_seq[17:18]
            samcut19 = sample_seq[18:19]
            samcut20 = sample_seq[19:20]
            samcut21 = sample_seq[20:21]
            samcut22 = sample_seq[21:22]
            samcut23 = sample_seq[22:23]
            samcut24 = sample_seq[23:24]
            samcut25 = sample_seq[24:25]
            samcut26 = sample_seq[25:26]
            samcut27 = sample_seq[26:27]
            samcut28 = sample_seq[27:28]
            samcut29 = sample_seq[28:29]
            samcut30 = sample_seq[29:]
            data = []
            data_num = []
            if cutseq1 != samcut1:
                cut1 = cutseq1 + samcut1
                cutnum1 = "1:2"
                data.append(cut1)
                data_num.append(cutnum1)
            if cutseq2 != samcut2:
                cut2 = cutseq2 + samcut2
                cutnum2 = "1:3"
                data.append(cut2)
                data_num.append(cutnum2)
            if cutseq3 != samcut3:
                cut3 = cutseq3 + samcut3
                cutnum3 = "1:4"
                data.append(cut3)
                data_num.append(cutnum3)
            if cutseq4 != samcut4:
                cut4 = cutseq4 + samcut4
                cutnum4 = "2:2"
                data.append(cut4)
                data_num.append(cutnum4)
            if cutseq5 != samcut5:
                cut5 = cutseq5 + samcut5
                cutnum5 = "2:3"
                data.append(cut5)
                data_num.append(cutnum5)
            if cutseq6 != samcut6:
                cut6 = cutseq6 + samcut6
                cutnum6 = "2:4"
                data.append(cut6)
                data_num.append(cutnum6)
            if cutseq7 != samcut7:
                cut7 = cutseq7 + samcut7
                cutnum7 = "3:2"
                data.append(cut7)
                data_num.append(cutnum7)
            if cutseq8 != samcut8:
                cut8 = cutseq8 + samcut8
                cutnum8 = "3:3"
                data.append(cut8)
                data_num.append(cutnum8)
            if cutseq9 != samcut9:
                cut9 = cutseq9 + samcut9
                cutnum9 = "3:4"
                data.append(cut9)
                data_num.append(cutnum9)
            if cutseq10 != samcut10:
                cut10 = cutseq10 + samcut10
                cutnum10 = "4:2"
                data.append(cut10)
                data_num.append(cutnum10)
            if cutseq11 != samcut11:
                cut11 = cutseq11 + samcut11
                cutnum11 = "4:3"
                data.append(cut11)
                data_num.append(cutnum11)
            if cutseq12 != samcut12:
                cut12 = cutseq12 + samcut12
                cutnum12 = "4:4"
                data.append(cut12)
                data_num.append(cutnum12)
            if cutseq13 != samcut13:
                cut13 = cutseq13 + samcut13
                cutnum13 = "5:2"
                data.append(cut13)
                data_num.append(cutnum13)
            if cutseq14 != samcut14:
                cut14 = cutseq14 + samcut14
                cutnum14 = "5:3"
                data.append(cut14)
                data_num.append(cutnum14)
            if cutseq15 != samcut15:
                cut15 = cutseq15 + samcut15
                cutnum15 = "5:4"
                data.append(cut15)
                data_num.append(cutnum15)
            if cutseq16 != samcut16:
                cut16 = cutseq16 + samcut16
                cutnum16 = "6:2"
                data.append(cut16)
                data_num.append(cutnum16)
            if cutseq17 != samcut17:
                cut17 = cutseq17 + samcut17
                cutnum17 = "6:3"
                data.append(cut17)
                data_num.append(cutnum17)
            if cutseq18 != samcut18:
                cut18 = cutseq18 + samcut18
                cutnum18 = "6:4"
                data.append(cut18)
                data_num.append(cutnum18)
            if cutseq19 != samcut19:
                cut19 = cutseq19 + samcut19
                cutnum19 = "7:2"
                data.append(cut19)
                data_num.append(cutnum19)
            if cutseq20 != samcut20:
                cut20 = cutseq20 + samcut20
                cutnum20 = "7:3"
                data.append(cut20)
                data_num.append(cutnum20)
            if cutseq21 != samcut21:
                cut21 = cutseq21 + samcut21
                cutnum21 = "7:4"
                data.append(cut21)
                data_num.append(cutnum21)
            if cutseq22 != samcut22:
                cut22 = cutseq22 + samcut22
                cutnum22 = "8:2"
                data.append(cut22)
                data_num.append(cutnum22)
            if cutseq23 != samcut23:
                cut23 = cutseq23 + samcut23
                cutnum23 = "8:3"
                data.append(cut23)
                data_num.append(cutnum23)
            if cutseq24 != samcut24:
                cut24 = cutseq24 + samcut24
                cutnum24 = "8:4"
                data.append(cut24)
                data_num.append(cutnum24)
            if cutseq25 != samcut25:
                cut25 = cutseq25 + samcut25
                cutnum25 = "9:2"
                data.append(cut25)
                data_num.append(cutnum25)
            if cutseq26 != samcut26:
                cut26 = cutseq26 + samcut26
                cutnum26 = "9:3"
                data.append(cut26)
                data_num.append(cutnum26)
            if cutseq27 != samcut27:
                cut27 = cutseq27 + samcut27
                cutnum27 = "9:4"
                data.append(cut27)
                data_num.append(cutnum27)
            if cutseq28 != samcut28:
                cut28 = cutseq28 + samcut28
                cutnum28 = "10:2"
                data.append(cut28)
                data_num.append(cutnum28)
            if cutseq29 != samcut29:
                cut29 = cutseq29 + samcut29
                cutnum29 = "10:3"
                data.append(cut29)
                data_num.append(cutnum29)
            if cutseq30 != samcut30:
                cut30 = cutseq30 + samcut30
                cutnum30 = "10:4"
                data.append(cut30)
                data_num.append(cutnum30)
            ouf.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li2[0], li2[1], li2[2], li2[3], li2[4],data, data_num))
ouf.close()
inf3 = [r for r in open("./scripts/temp/hse3.txt","r")]
ouf1 = open("./scripts/temp/hse4.txt","w")
for line3 in inf3:
    li3 = line3.strip()
    li3 = li3.replace("'","").replace("[","").replace("]","").strip()
    li3 = re.split(",|\t",li3)
    if len(li3) == 7:
        ouf1.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li3[0],li3[1],li3[2],li3[3],li3[4],li3[5],li3[6]))
    if len(li3) == 5:
        ouf1.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (li3[0],li3[1],li3[2],li3[3],li3[4],"NA","NA"))
ouf1.close()
