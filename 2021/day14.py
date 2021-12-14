#Solution for https://adventofcode.com/2021/day/14 by Kelvin Yip
import numpy as np
polymer = "OOBFPNOPBHKCCVHOBCSO"
directionslist = ["NS -> H",
"NN -> P",
"FF -> O",
"HF -> C",
"KN -> V",
"PO -> B",
"PS -> B",
"FB -> N",
"ON -> F",
"OK -> F",
"OO -> K",
"KS -> F",
"FN -> F",
"KC -> H",
"NC -> N",
"NB -> C",
"KH -> S",
"SV -> B",
"BC -> S",
"KB -> B",
"SC -> S",
"KP -> H",
"FS -> K",
"NK -> K",
"OC -> H",
"NH -> C",
"PH -> F",
"OS -> V",
"BB -> C",
"CC -> F",
"CF -> H",
"CP -> V",
"VB -> N",
"VC -> F",
"PK -> V",
"NV -> N",
"FO -> S",
"CK -> O",
"BH -> K",
"PN -> B",
"PP -> S",
"NF -> B",
"SF -> K",
"VF -> H",
"HS -> F",
"NP -> F",
"SH -> V",
"SK -> K",
"PC -> V",
"BO -> H",
"HN -> P",
"BK -> O",
"BP -> S",
"OP -> N",
"SP -> N",
"KK -> C",
"HB -> H",
"OF -> C",
"VH -> C",
"HO -> N",
"FK -> V",
"NO -> H",
"KF -> S",
"KO -> V",
"PF -> K",
"HV -> C",
"SO -> F",
"SS -> F",
"VN -> K",
"HH -> B",
"OB -> S",
"CH -> B",
"FH -> B",
"CO -> V",
"HK -> F",
"VK -> K",
"CN -> V",
"SB -> K",
"PV -> O",
"PB -> F",
"VV -> P",
"CS -> N",
"CB -> C",
"BS -> F",
"HC -> B",
"SN -> P",
"VP -> P",
"OV -> P",
"BV -> P",
"FC -> N",
"KV -> S",
"CV -> F",
"BN -> S",
"BF -> C",
"OH -> F",
"VO -> B",
"FP -> S",
"FV -> V",
"VS -> N",
"HP -> B"]


#Part 1 brute force method
directions = {}
for guy in directionslist:
    directions[guy[:2]] = guy[-1]

newstring = polymer
for i in range(10):
    teststring = newstring[0]
    for j in newstring[1:]:
        teststring += directions[teststring[-1] + j]
        teststring += j
    newstring = teststring
most = 0
least = np.inf

letters = []
for i in newstring:
    if i not in letters:
        letters.append(i)
        if newstring.count(i) > most:
            most = newstring.count(i)

        if newstring.count(i) < least:
            least = newstring.count(i)

print(most, least, most-least)


#Part 2 Slightly less brute force
#Unfortunately slower than I would have liked(around a minute to fully run), but at least it works
count20 = {}
#After enough iterations, the letters that show up the most and least will remain the same
#In the case of this given input, the letter that is most frequent is 'K', and the least frequent 'O'
#For each two letter pair in directions, we calculate count('K') - count('O') after 20 iterations
#The count is then added to another dictionary, 'count20', using the same two letter key
for key in directions:
    newstring = key
    for i in range(20):
        teststring = newstring[0]
        for j in newstring[1:]:
            teststring += directions[teststring[-1] + j]
            teststring += j
        newstring = teststring
    count20[key] = newstring.count('K') - newstring.count('O')

#We then find the resulting string after 20 iterations of the full starting polymer
newstring = polymer
for i in range(20):
    teststring = newstring[0]
    for j in newstring[1:]:
        teststring += directions[teststring[-1] + j]
        teststring += j
    newstring = teststring

#Instead of trying to iterate 20 more times, we simply check every two adjacent letters in the 20 step polymer
#and check their definition in count20 and add it to the existing count
count = 0
for i in range(0, len(newstring)-1):
    count += count20[newstring[i:i+2]]

#To avoid double counting, due to each letter being counted twice, we subtract any K's and add any O's onto the count
#Because the ends of the polymer are counted only once however, and the ends are O's, we subtract 2 to avoid oversubtracting
count -= newstring.count('K')-newstring.count('O')
count -= 2
print(count)