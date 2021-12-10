#Solution for https://adventofcode.com/2021/day/2 created by Kelvin Yip on 12/1/2021
#Sample input used as actual input is huge as heck

puzzleinput = ["forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2"
]

#Part 1
start = [0,0]
for i in puzzleinput:
    a = i[:i.index(' ')]
    b = int(i[-1])
    if a == 'forward':
        start[0]+= b
    elif a == 'up':
        start[1] += b
    else:
        start[1] -= b
print(start[0]*start[1])


#Part 2
aim = 0
pos = 0
depth = 0
for i in puzzleinput:
    a = i[:i.index(' ')]
    b = int(i[-1])
    if a == 'forward':
        pos += b
        depth += aim * b
    elif a == 'up':
        aim += b
    else:
        aim -= b
print(pos*depth)





