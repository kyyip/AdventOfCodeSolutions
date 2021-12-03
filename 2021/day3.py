#Solution for https://adventofcode.com/2021/day/3 created by Kelvin Yip on 12/2/2021
#Sample input, real input big boi
puzzleinput=["00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]
gamma = ""
epsilon = ""

#Part 1
for i in range(len(puzzleinput[0])):
    zeros = 0
    ones = 0
    for j in range(len(puzzleinput)):
        if puzzleinput[j][i] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

def decfunc(binarystr):
    dec = 0
    for i in range(len(binarystr)):
        dec += int(binarystr[-i-1]) * 2 ** i
    return dec
print(decfunc(gamma) * decfunc(epsilon))


#Part 2
def oxyfunc(numbers, bit=0):
    if len(numbers) == 1:
        return numbers[0]
    else:
        newnumbers = []
        zeros = 0
        ones = 0
        for i in range(len(numbers)):
            if numbers[i][bit] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            for number in numbers:
                if number[bit] == "0":
                    newnumbers.append(number)
        else:
            for number in numbers:
                if number[bit] == "1":
                    newnumbers.append(number)
        return(oxyfunc(newnumbers, bit+1))
oxy = oxyfunc(puzzleinput)

def carbonfunc(numbers, bit=0):
    if len(numbers) <= 1:
        return numbers[0]
    newnumbers = []
    zeros = 0
    ones = 0
    for i in range(len(numbers)):
        if numbers[i][bit] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros <= ones:
        for number in numbers:
            if number[bit] == "0":
                newnumbers.append(number)
    else:
        for number in numbers:
            if number[bit] == "1":
                newnumbers.append(number)
    return(carbonfunc(newnumbers, bit+1))
carb = carbonfunc(puzzleinput)
print(decfunc(oxy) * decfunc(carb))


