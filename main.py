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

for time in time_2:
    for j in bnz_set:
        if j == time_2[time]:
            for q in bnz_set[j]:

                if time > str(ready):
                    if 0 < kol_1:
                        kol_1 -= 1
                    elif 0 < kol_2:
                        kol_2 -= 1
                    elif 0 < kol_3:
                        kol_3 -= 1

                skor = math.ceil(int(time_3[time]) / 10)
                a = time
                x = int(a[3:]) + skor
                if x < 10:
                    x = '0' + str(x)
                if int(x) > 60:
                    if int(a[:2]) == 23:
                        c = str(x - 60)
                        y = '00'
                    else:
                        y = str(int(a[:2]) + 1)
                        c = str(int(a[:2]) + x - 60)
                    if len(c) == 1:
                        c = '0' + c
                    ready = y + ':' + c
                else:
                    ready = a[:3] + str(x)

                if kol_1 < int(queue[q]):
                    kol_1 += 1
                    all_text = lc.IN + time + lc.NEW_CLIENT + time + ' ' + time_2[time] + \
                               ' ' + time_3[time] + ' ' + str(kol_1) + lc.QUEUE + q
                    left = lc.IN + str(ready) + lc.CLIENT + time + ' ' + time_2[time] + \
                           ' ' + time_3[time] + ' ' + str(kol_1) + lc.DONE

                elif kol_2 < int(queue[q]):
                    kol_2 += 1
                    all_text = lc.IN + time + lc.NEW_CLIENT + time + ' ' + time_2[time] + \
                               ' ' + time_3[time]  + ' ' + str(kol_2) + lc.QUEUE + q
                    left = lc.IN + str(ready) + lc.CLIENT + time + ' ' + time_2[time] + \
                           ' ' + time_3[time] + ' ' + str(kol_2) + lc.DONE

                elif kol_3 < int(queue[q]):
                    kol_3 += 1
                    all_text = lc.IN + time + lc.NEW_CLIENT + time + ' ' + time_2[time] + \
                               ' ' + time_3[time] + ' ' + str(kol_3) + lc.QUEUE + q
                    left = lc.IN + str(ready) + lc.CLIENT + time + ' ' + time_2[time] + \
                           ' ' + time_3[time] + ' ' + str(kol_3) + lc.DONE

                else:
                    all_text = lc.IN + time + lc.NEW_CLIENT + time + ' ' + time_2[time] + \
                               ' ' + time_3[time] + ' ' + lc.LEFT
                    no_catch += 1
                    time_1[time_2[time]] = time_1.get(time_2[time], 0) - int(time_3[time])
                print(all_text)
                text = ''
                ben_nam = ''
                for w in queue:
                    n = convertation(bnz_reverse[w])
                    if w in 'kol_1':
                        text += lc.MACHINE + w + ' ' + lc.MAX_QUEUE + \
                                queue[w] + ' ' + lc.BENZ + n + '->' + '*' * kol_1
                    elif w in 'kol_2':
                        text += lc.MACHINE + w + ' ' + lc.MAX_QUEUE + \
                                queue[w] + ' ' + lc.BENZ + n + '->' + '*' * kol_2
                    else:
                        text += lc.MACHINE + w + ' ' + lc.MAX_QUEUE + \
                                queue[w] + ' ' + lc.BENZ + n + '->' + '*' * kol_3
                    print(text)
                    text = ''
                if left != '':
                    print(left)
                    text = ''
                    ben_nam = ''
                    for w in queue:
                        n = convertation(bnz_reverse[w])
                        if w in 'kol_1':
                            text += lc.MACHINE + w + ' ' + lc.MAX_QUEUE + \
                                    queue[w] + ' ' + lc.BENZ + n + '->' + '*' * (kol_1 - 1)
                        elif w in 'kol_2':
                            text += lc.MACHINE + w + ' ' + lc.MAX_QUEUE + \
                                    queue[w] + ' ' + lc.BENZ + n + '->' + '*' * (kol_2 - 1)
                        else:
                            text += lc.MACHINE + w + ' ' + lc.MAX_QUEUE + \
                                    queue[w] + ' ' + lc.BENZ + n + '->' + '*' * (kol_3 - 1)
                        print(text)
                        text = ''
                left = ''
                break
print('')
print(lc.PRINT1, no_catch)
for number in time_1:
    print(lc.PRINT2 + str(number) + ': ' + str(time_1[number]))

sales_amount = 0
for number in time_1:
    number_price = int(bnz_price[number])
    number_value = int(time_1[number])
    sales_amount += number_price * number_value
print(lc.PRINT3, sales_amount)
