#Solution for https://adventofcode.com/2021/day/5 by Kelvin Yip
import numpy as np
#Using sample input as actual input has a 1000x1000 sea floor
puzzleinput = ["0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2"
]
#Formatting puzzle input into integer coordinates and including sea floor
lines = []
newlines = []
floor = [[0 for i in range(1000)] for j in range(1000)]
for i in puzzleinput:
    lines.append(((i[:i.index("->")-1]), i[i.index("->")+3:]))
for line in lines:
    newlines.append([(int(line[0][:line[0].index(',')]), int(line[0][line[0].index(',')+1:])),
                     (int(line[1][:line[1].index(',')]), int(line[1][line[1].index(',')+1:]))])

#Check for horizontal/vertical lines between coordinates
for line in newlines:
    if line[0][0] == line[1][0]:
        axis = line[0][0]
        path = [line[0][1], line[1][1]]
        path.sort()
        for i in range(path[0],path[1]+1):
            floor[axis][i] += 1
    elif line[0][1] == line[1][1]:
        axis = line[0][1]
        path = [line[0][0], line[1][0]]
        path.sort()
        for i in range(path[0],path[1]+1):
            floor[i][axis] += 1
#Check for diagonal lines in part 2
    else:
        diff = np.array(line[0]) - np.array(line[1])
        if abs(diff[0]) == abs(diff[1]):
            steps = abs(diff[0])
            where = -(diff)/steps
            for i in range(steps + 1):
                floor[line[0][0] + int(i*where[0])][line[0][1] + int(i*where[1])] += 1
            
        
count = 0
for line in floor:
    for i in line:
        if i >= 2:
            count += 1
print(count)




