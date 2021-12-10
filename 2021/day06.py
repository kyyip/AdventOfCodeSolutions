#Solution for https://adventofcode.com/2021/day/6 by Kelvin Yip
#Real input used as it is short enough to fit
puzzleinput = [1,3,3,4,5,1,1,1,1,1,1,2,1,4,1,1,1,5,2,2,4,3,1,1,2,5,4,2,2,3,1,2,3,2,1,1,4,4,2,4,4,1,2,4,3,3,3,1,1,3,4,5,2,5,1,2,5,1,1,1,3,2,3,3,1,4,1,1,4,1,4,1,1,1,1,5,4,2,1,2,2,5,5,1,1,1,1,2,1,1,1,1,3,2,3,1,4,3,1,1,3,1,1,1,1,3,3,4,5,1,1,5,4,4,4,4,2,5,1,1,2,5,1,3,4,4,1,4,1,5,5,2,4,5,1,1,3,1,3,1,4,1,3,1,2,2,1,5,1,5,1,3,1,3,1,4,1,4,5,1,4,5,1,1,5,2,2,4,5,1,3,2,4,2,1,1,1,2,1,2,1,3,4,4,2,2,4,2,1,4,1,3,1,3,5,3,1,1,2,2,1,5,2,1,1,1,1,1,5,4,3,5,3,3,1,5,5,4,4,2,1,1,1,2,5,3,3,2,1,1,1,5,5,3,1,4,4,2,4,2,1,1,1,5,1,2,4,1,3,4,4,2,1,4,2,1,3,4,3,3,2,3,1,5,3,1,1,5,1,2,2,4,4,1,2,3,1,2,1,1,2,1,1,1,2,3,5,5,1,2,3,1,3,5,4,2,1,3,3,4
]


#Part 1, brute force method

for i in range(80):
    count=0
    for i in range(len(puzzleinput)):
        if puzzleinput[i] == 0:
            puzzleinput[i] = 6
            count += 1
        else:
            puzzleinput[i] -= 1
    for i in range(count):
        puzzleinput.append(8)

print(len(puzzleinput))




#Part 2, slightly less brute force method
puzzleinput = [1,3,3,4,5,1,1,1,1,1,1,2,1,4,1,1,1,5,2,2,4,3,1,1,2,5,4,2,2,3,1,2,3,2,1,1,4,4,2,4,4,1,2,4,3,3,3,1,1,3,4,5,2,5,1,2,5,1,1,1,3,2,3,3,1,4,1,1,4,1,4,1,1,1,1,5,4,2,1,2,2,5,5,1,1,1,1,2,1,1,1,1,3,2,3,1,4,3,1,1,3,1,1,1,1,3,3,4,5,1,1,5,4,4,4,4,2,5,1,1,2,5,1,3,4,4,1,4,1,5,5,2,4,5,1,1,3,1,3,1,4,1,3,1,2,2,1,5,1,5,1,3,1,3,1,4,1,4,5,1,4,5,1,1,5,2,2,4,5,1,3,2,4,2,1,1,1,2,1,2,1,3,4,4,2,2,4,2,1,4,1,3,1,3,5,3,1,1,2,2,1,5,2,1,1,1,1,1,5,4,3,5,3,3,1,5,5,4,4,2,1,1,1,2,5,3,3,2,1,1,1,5,5,3,1,4,4,2,4,2,1,1,1,5,1,2,4,1,3,4,4,2,1,4,2,1,3,4,3,3,2,3,1,5,3,1,1,5,1,2,2,4,4,1,2,3,1,2,1,1,2,1,1,1,2,3,5,5,1,2,3,1,3,5,4,2,1,3,3,4
]
steps128 = []
fishes128 = []
steps256 = []
#Find list and list length for 128 steps for a starting input of [i] for i in range(0,8)
for boi in range(0, 9):
    sampleinput = [boi]
    for i in range(128):
        count = 0
        for j in range(len(sampleinput)):
            if sampleinput[j] >0:
                sampleinput[j] = sampleinput[j]-1
            else:
                sampleinput[j]=6
                count += 1
        for k in range(count):
            sampleinput.append(8)
    steps128.append(len(sampleinput))
    fishes128.append(sampleinput)

#Then calculate the list length for a 256 step sequence of starting input [i] for i from 1 to 5 by taking each 128 step list for i and then taking the sum of each integers 128step sequence length derived earlier
#We only need 1 to 5 and the puzzle input only has integers from 1 to 5
for fishes in fishes128[1:6]:
    totes = 0
    for fish in fishes:
        totes += steps128[fish]
    steps256.append(totes)
final = 0
#Finally calculate the length of the 256 step sequence for our puzzle input using the length of each 256 step sequence for [i] from 1 to 5 calculated in the previous step
for i in puzzleinput:
    final += steps256[i-1]
print(final)
