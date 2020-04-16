''' Case study Dictionaries
Developers: Arkhipova A.(%)
            Revtova L.(%)
'''
import math
import local


choose = int(input(local.CHOOSE))
if choose == 1:
    import local_english as lc
elif choose == 2:
    import local_russian as lc

no_catch = 0
ready = 0
kol_1 = 0
kol_2 = 0
kol_3 = 0
bnz_set = {}
bnz_reverse = {}
queue = {}
time_1 = {}
time_2 = {}
time_3 = {}
bnz_price = {}
digits = '0123456789'
left = ''
all_text = ''


def convertation(lst):
    s = ''
    for i in lst:
        i = str(i)
        s = s + i + ', '
    return s[:-2]


with open("input.txt", encoding='utf-8') as inp:
    for i in inp:
        line = i.split()
        time_2[line[0]] = line[-1]
        time_3[line[0]] = line[1]
        time_1[line[2]] = time_1.get(line[2], 0) + int(line[1])

with open("azs.txt", encoding='utf-8') as azs:
    for i in azs:
        line = i.split()
        queue[line[0]] = line[1]
        bnz_reverse[line[0]] = line[2:]
        for j in line:
            if j not in digits:
                if j not in bnz_set:
                    bnz_set[j] = [line[0]]
                else:
                    bnz_set[j] += line[0]

with open("price.txt", encoding='utf-8') as price:
    for i in price:
        prc = i.split()
        bnz_price[prc[0]] = int(prc[-1])
