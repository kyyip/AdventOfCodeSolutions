#Solution for https://adventofcode.com/2021/day/8 by Kelvin Yip
#Sample input because real input is a big boi
puzzleinput = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
"edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
"fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
"fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
"aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
"fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
"dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
"bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
"egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
"gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
]


#Part 1, find 1, 4, 7, 8
#Very easy
count = 0
for line in puzzleinput:
    segment = line[line.index("|")+2:].split()
    for boi in segment:
        if len(boi) in [2,3,4,7]:
            count += 1
print(count)


#Part 2, find the rest of the numbers
#Detective time
tot = 0
for line in puzzleinput:
    start = line[:line.index("|")-1].split()
    numbers = {}
    
    #Start by pulling out segments for 1, 4, 7, and 8
    for i in start:
        if len(i) == 2:
            numbers[1] = set([j for j in i])
            start.remove(i)
            break
    for i in start:
        if len(i) == 3:
            numbers[7] = set([j for j in i])
            start.remove(i)
            break
    for i in start:
        if len(i) == 4:
            numbers[4] = set([j for j in i])
            start.remove(i)
            break
    for i in start:
        if len(i) == 7:
            numbers[8] = set([j for j in i])
            start.remove(i)
            break
            
    #6 is the only 6 segment number which contains the difference 8 and 7 as a subset
    for i in start:
        if len(i) == 6 and numbers[8].difference(numbers[7]).issubset(set([j for j in i])):
            numbers[6] = set([j for j in i])
            start.remove(i)
            break
            
    #5 is the only 5 segment number that is a subset of 6
    for i in start:
        if len(i) == 5 and set([j for j in i]).issubset(numbers[6]):
            numbers[5] = set([j for j in i])
            start.remove(i)
            break
            
    #9 is the only 6 segment number that contains the union of 1 and 5 as a subset
    for i in start:
        if len(i) == 6 and numbers[1].union(numbers[5]) == set([j for j in i]):
            numbers[9] = set([j for j in i])
            start.remove(i)
            break
            
    #0 is the only number not to be removed that contains 6 segments 
    for i in start:
        if len(i) == 6:
            numbers[0] = set([j for j in i])
            start.remove(i)
            break
            
    #2 and 3 remain, 1 is a subset of 3 and not 2
    for i in start:
        if numbers[1].issubset(set([j for j in i])):
            numbers[3] = set([j for j in i])
            start.remove(i)
            
    #2 is the last guy
    numbers[2] = set([j for j in start[0]])
    segment = line[line.index("|")+2:].split()
    final = ""
    #Decipher the four digit code and add to summation for final answer
    for boi in segment:
        boiset = set([j for j in boi])
        for number in numbers:
            if numbers[number] == boiset:
                final += str(number)
                break
    tot += int(final)
print(tot)


# In[ ]:




