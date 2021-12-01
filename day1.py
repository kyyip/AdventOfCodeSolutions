#Solution for https://adventofcode.com/2021/day/1 created on 11/30/2021 by Kelvin Yip
#Sample input used as actual input is extremely large

#Part 1
depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
counts = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        counts += 1
print(counts)

#Part 2
counts2 = 0
for i in range(1, len(depths)-2):
    if depths[i+2] > depths[i-1]:
        counts2 += 1
print(counts2)




