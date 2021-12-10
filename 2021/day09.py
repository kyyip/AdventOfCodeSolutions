#Solution for https://adventofcode.com/2021/day/9 by Kelvin Yip
#Sample input because the real input too stronk for human eyes
vents = ["2199943210",
"3987894921",
"9856789892",
"8767896789",
"9899965678"
]


#Part 1, storing coordinates of each basin for part 2
heat = 0
basins = []
for i in range(len(vents)):
    for j in range(len(vents[0])):
        basin = True
        if i-1 >= 0:
            if vents[i-1][j] <= vents[i][j]:
                basin = False
        if i+1 < len(vents) and basin:
            if vents[i+1][j] <= vents[i][j]:
                basin = False
        if j-1 >= 0 and basin:
            if vents[i][j-1] <= vents[i][j]:
                basin = False
        if j+1 < len(vents[0]) and basin:
            if vents[i][j+1] <= vents[i][j]:
                basin = False
        if basin:
            basins.append([i,j])
            heat += 1 + int(vents[i][j])
print(heat)

#Part 2
area = 0
biggest = [0, 0, 0]
covered = []

def basinfunc(i, j):
    global area
    global vents
    global covered
    covered.append([i, j])
    area += 1
    if i-1 >= 0 and [i-1, j] not in covered and vents[i-1][j] != "9":
        basinfunc(i-1, j)
    if i+1 < len(vents) and [i+1, j] not in covered and vents[i+1][j] != "9":
        basinfunc(i+1, j)
    if j-1 >= 0 and [i, j-1] not in covered and vents[i][j-1] != "9":
        basinfunc(i, j-1)
    if j+1 < len(vents[0]) and [i, j+1] not in covered and vents[i][j+1] != "9":
        basinfunc(i, j+1)

for basin in basins:
    covered = []
    area = 0
    basinfunc(basin[0], basin[1])
    if area > biggest[0]:
        biggest[0] = area
        biggest.sort()
print(biggest[0]*biggest[1]*biggest[2])
    
#Bonus, the solution for part 1 I came up with when solving the problem for the first time
#A good example of how solving under pressure makes you code like an idiot :)
"""
heat = 0
basins = []
if vents[0][0] < vents[1][0] and vents[0][0] < vents[0][1]:
    heat += 1 + int(vents[0][0])
    basins.append([0,0])
    
if vents[0][len(vents[0])-1] < vents[1][len(vents[0])-1] and vents[0][len(vents[0])-1] < vents[0][len(vents[0])-2]:
    heat += 1 + int(vents[0][len(vents[0])-1])
    basins.append([0, len(vents[0])-1])
    
if vents[len(vents)-1][0] < vents[len(vents)-1][1] and vents[len(vents)-1][0] < vents[len(vents)-2][0]:
    heat += 1 + int(vents[len(vents)-1][0])
    basins.append([len(vents)-1, 0])

if vents[len(vents)-1][len(vents[0])-1] < vents[len(vents)-2][len(vents[0])-1] and vents[len(vents)-1][len(vents[0])-1] < vents[len(vents)-1][len(vents[0])-2]:
    heat += 1 + int(vents[len(vents)-1][len(vents[0])-1])
    basins.append([len(vents)-1, len(vents[0])-1])
    
for i in range(1, len(vents[0])-1):
    if vents[0][i] < vents[0][i-1] and vents[0][i] < vents[0][i+1] and vents[0][i] < vents[1][i]:
        heat += 1 + int(vents[0][i])
        basins.append([0, i])
        
    if vents[len(vents)-1][i] < vents[len(vents)-1][i-1] and vents[len(vents)-1][i] < vents[len(vents)-1][i+1] and vents[len(vents)-1][i] < vents[len(vents)-2][i]:
        heat += 1 + int(vents[len(vents)-1][i])
        basins.append([len(vents)-1, i])

for i in range(1, len(vents)-1):
    if vents[i][0] < vents[i-1][0] and vents[i][0] < vents[i+1][0] and vents[i][0] < vents[i][1]:
        heat += 1 + int(vents[i][0])
        basins.append([i, 0])
    if vents[i][len(vents[0])-1] < vents[i-1][len(vents[0])-1] and vents[i][len(vents[0])-1] < vents[i+1][len(vents[0])-1] and vents[i][len(vents[0])-1] < vents[i][len(vents[0])-2]:
        heat += 1 + int(vents[i][len(vents[0])-1])
        basins.append([i, len(vents[0])-1])

for i in range(1, len(vents) - 1):
    for j in range(1, len(vents[0]) - 1):
        if vents[i][j] < vents[i-1][j] and vents[i][j] < vents[i+1][j] and vents[i][j] < vents[i][j-1] and vents[i][j] < vents[i][j+1]:
            heat += 1 + int(vents[i][j])
            basins.append([i,j])
print(heat)
print(basins)
"""
