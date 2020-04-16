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
