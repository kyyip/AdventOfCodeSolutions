#'Solution' for https://adventofcode.com/2021/day/24 by Kelvin Yip
#Short essay below puzzleinput explaining how I found the solutions.
puzzleinput = ["inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 1",
"add x 13",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 10",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 1",
"add x 11",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 16",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 1",
"add x 11",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 0",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 1",
"add x 10",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 13",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 26",
"add x -14",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 7",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 26",
"add x -4",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 11",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 1",
"add x 11",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 11",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 26",
"add x -3",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 10",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 1",
"add x 12",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 16",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 26",
"add x -12",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 8",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 1",
"add x 13",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 15",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 26",
"add x -12",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 2",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 26",
"add x -15",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 5",
"mul y x",
"add z y",
"inp w",
"mul x 0",
"add x z",
"mod x 26",
"div z 26",
"add x -12",
"eql x w",
"eql x 0",
"mul y 0",
"add y 25",
"mul y x",
"add y 1",
"mul z y",
"mul y 0",
"add y w",
"add y 10",
"mul y x",
"add z y"]


#This problem involved mostly trial and error. I started by writing the interpreter function which would
#take a 14 digit number and the list of instructions and return the final value for z. The function would
#also print out on each step the value of the dimension that was being operated on. This allows you to see
#how the values were being manipulated at each step. In this particular input, there were steps where the
#code would check if 'x' equaled 'w' and if it was true, 'z' would always be reduced. Given that 'w' is determined
#by the digits of our starting number, we can modify the digits of our starting number so that 'x' == 'w' whenever
#possible until eventually, our z value is 0. For part 1, we start with 999999999999999 and modify accordingly.
#For part 2, we do much of the same except start with 11111111111111. While I did find the solutions manually, you can
#with a little more effort automate finding the solution.
from math import floor
instructions = []
for i in puzzleinput:
    instructions.append(i.split())


def alufunc(numb, instructions):
    digit = 0
    dims = {'w':0, 'x': 0, 'y':0, 'z':0}
    for idx, i in enumerate(instructions):
        if i[0] == 'inp':
            dims[i[1]] = int(numb[digit])
            digit += 1
        elif i[0] == 'add':
            if i[2] in dims:
                dims[i[1]] += dims[i[2]]
            else:
                dims[i[1]] += int(i[2])
        elif i[0] == 'mul':
            if i[2] in dims:
                dims[i[1]] *= dims[i[2]]
            else:
                dims[i[1]] *= int(i[2])
        elif i[0] == 'div':
            if i[2] in dims:
                dims[i[1]] = floor(dims[i[1]]/dims[i[2]])
            else:
                dims[i[1]] = floor(dims[i[1]]/int(i[2]))
        elif i[0] == 'mod':
            if i[2] in dims:
                dims[i[1]] = dims[i[1]]%dims[i[2]]
            else:
                dims[i[1]] = dims[i[1]]%int(i[2])
        elif i[0] == 'eql':
            if i[2] in dims:
                if dims[i[1]] == dims[i[2]]:
                    dims[i[1]] = 1
                else:
                    dims[i[1]] = 0
            else:
                if dims[i[1]] == int(i[2]):
                    dims[i[1]] = 1
                else:
                    dims[i[1]] = 0
#Print step is commented out to avoid cluttering up the screen
            #print(digit, i, i[1], dims[i[1]])
    return(dims['z'])

#Arbitrary 14 digit number to show that the function works
print('01234567891011', alufunc('01234567891011', instructions))
#Solution for part 1
print('98998519596997', alufunc('98998519596997', instructions))
#Solution for part 2
print('31521119151421', alufunc('31521119151421', instructions))