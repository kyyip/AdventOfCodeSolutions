#Solution for https://adventofcode.com/2021/day/18 by Kelvin Yip
#There's probably a way to do this using lists instead of strings, but I'm a string manipulation god(not really)
snails = ["[[4,[3,[2,8]]],[[[8,5],4],[[3,5],[4,9]]]]",
"[[[8,[6,8]],2],[4,[[1,0],[4,5]]]]",
"[[4,3],[[[3,3],[1,8]],[[0,8],[5,8]]]]",
"[[[8,[5,8]],[[8,7],[2,1]]],[3,[[0,3],1]]]",
"[[9,[[9,2],3]],[3,[[9,7],[2,8]]]]",
"[[[7,[0,0]],[[4,3],[6,3]]],[6,[4,5]]]",
"[[[[4,2],[0,0]],[4,2]],[[[8,7],8],[[9,4],5]]]",
"[[4,[1,[1,1]]],[[[0,6],8],[[7,5],[7,3]]]]",
"[[[1,[9,9]],[4,3]],[[1,[5,8]],9]]",
"[[2,[6,[6,7]]],[[6,[1,5]],8]]",
"[4,[[[9,8],[1,3]],[7,[7,4]]]]",
"[[[[2,6],8],2],[[[2,2],8],[[3,7],8]]]",
"[[[[1,5],2],[[8,9],[8,3]]],[[[7,3],[1,1]],[[3,7],7]]]",
"[[[4,4],[8,9]],[5,3]]",
"[[[[1,4],[4,5]],9],[[2,8],0]]",
"[[[[4,4],[7,3]],[[9,7],[3,9]]],[9,[5,[5,1]]]]",
"[[5,[[5,9],6]],[[[5,9],[6,3]],1]]",
"[[[[1,0],[1,6]],5],[1,9]]",
"[[[[6,3],[7,2]],1],[[0,6],6]]",
"[[[3,4],[4,0]],[[[6,4],[2,0]],[7,[7,2]]]]",
"[[[[1,3],[9,6]],[[1,1],[9,3]]],[[3,8],[[9,5],2]]]",
"[[[[9,4],6],5],[[[7,6],[2,3]],[6,6]]]",
"[[6,[2,[0,7]]],[[3,0],[8,[1,9]]]]",
"[[[6,0],[1,7]],[[[4,2],[5,7]],[[5,0],9]]]",
"[[[7,[4,9]],0],[[5,[7,5]],[8,[5,1]]]]",
"[[[[6,1],[8,0]],[3,[4,5]]],[[[8,3],4],[0,2]]]",
"[[[[3,8],5],[4,8]],9]",
"[[0,[7,[9,4]]],[2,2]]",
"[[[[9,6],[4,0]],[1,1]],[3,[[3,6],8]]]",
"[[[6,[3,3]],[[7,6],3]],[[[2,8],[0,7]],3]]",
"[[[[3,2],[2,4]],[[8,7],7]],[[[0,2],[1,3]],[8,3]]]",
"[[[[4,2],[6,8]],6],[[[2,1],[0,3]],[[6,6],[5,6]]]]",
"[[[[9,0],[1,7]],[[0,3],1]],[[0,[4,3]],7]]",
"[[[1,[1,4]],1],[[[8,1],9],[[7,1],[7,2]]]]",
"[2,[2,[[4,2],2]]]",
"[6,0]",
"[[[[9,7],7],[2,3]],[[8,[9,4]],[2,3]]]",
"[[[[4,5],8],6],[5,9]]",
"[[[5,[6,7]],[[1,9],[8,6]]],7]",
"[7,[[0,5],4]]",
"[[[2,4],[2,[1,9]]],[8,[5,6]]]",
"[3,[[6,[4,8]],[[3,0],9]]]",
"[[[[4,4],[0,5]],[7,3]],[1,[4,5]]]",
"[8,[[2,[1,1]],9]]",
"[[[[5,6],[5,1]],[[7,6],[8,8]]],[2,[[2,1],[3,1]]]]",
"[[0,[2,[4,6]]],[[[6,0],[3,9]],[0,[1,6]]]]",
"[[[6,[9,5]],[0,[9,4]]],0]",
"[[[[5,6],[7,8]],[7,[8,8]]],[[7,[4,7]],[[3,9],7]]]",
"[1,0]",
"[[7,2],[9,[3,0]]]",
"[[[[4,8],9],[1,[0,4]]],[[[5,2],0],8]]",
"[[[9,[2,5]],[2,[5,8]]],[1,6]]",
"[[[[0,5],1],[0,4]],7]",
"[8,[5,9]]",
"[[[[8,8],[4,8]],[[7,8],7]],[[0,4],8]]",
"[[[0,6],[9,6]],2]",
"[[[[2,5],[0,6]],8],[[8,9],1]]",
"[[[0,9],[1,[1,2]]],[[[4,1],6],7]]",
"[[[[5,7],[4,6]],[[6,3],[8,2]]],[[[2,5],[0,9]],[5,1]]]",
"[[[5,0],[[4,5],[6,2]]],[[[1,7],[3,0]],[[8,2],[6,1]]]]",
"[[[[8,9],9],[9,0]],[4,[[7,2],9]]]",
"[[[[2,3],[0,5]],[8,8]],[9,[[9,1],8]]]",
"[[[5,9],[0,[6,2]]],[[3,2],[[1,2],[9,5]]]]",
"[[[5,2],[8,[0,0]]],[[6,9],[4,[8,4]]]]",
"[7,3]",
"[[[6,4],[[0,4],7]],[[5,[0,3]],[8,7]]]",
"[[1,2],[[3,[5,9]],0]]",
"[[[6,9],[3,0]],[[[2,1],4],6]]",
"[[[8,[7,9]],1],[[[2,2],8],8]]",
"[[[0,1],[6,[3,3]]],5]",
"[[[[3,9],0],7],2]",
"[[[3,0],[1,[7,6]]],0]",
"[[[[3,5],3],8],[[[1,2],[8,8]],[[1,6],[8,1]]]]",
"[[[9,7],[[1,3],[6,9]]],6]",
"[[[[1,8],1],[[6,4],[1,8]]],[[[1,7],[5,9]],[[7,0],0]]]",
"[[[1,[9,3]],[4,0]],7]",
"[[5,[9,6]],[[4,[0,8]],2]]",
"[3,[[1,0],[0,2]]]",
"[[[3,1],[2,7]],[[4,4],5]]",
"[[8,6],[[4,[5,9]],[[3,7],9]]]",
"[[[3,2],2],[[3,9],8]]",
"[[[[4,5],[4,5]],[[0,2],[7,0]]],[[1,4],2]]",
"[7,[[8,[3,8]],[[5,6],4]]]",
"[[[[2,8],[2,2]],[[4,4],0]],[[2,[8,0]],2]]",
"[4,[[[8,8],0],[[1,8],[4,6]]]]",
"[[[5,[1,2]],7],9]",
"[[9,[[0,0],9]],[[5,[1,3]],[4,[4,7]]]]",
"[[3,4],[8,[2,[9,6]]]]",
"[[[[3,0],1],[[7,6],[5,2]]],[[[9,9],[9,2]],[0,[2,2]]]]",
"[[[[0,8],[6,1]],[2,0]],[6,[[8,8],[9,1]]]]",
"[[[5,[1,9]],6],6]",
"[[[3,5],[[9,9],[2,2]]],[[1,0],4]]",
"[[4,0],[2,[[8,8],[5,4]]]]",
"[[6,1],5]",
"[[[2,[3,7]],0],[1,5]]",
"[[[[5,9],[5,3]],[6,2]],[[7,9],4]]",
"[[[5,[0,9]],[[5,6],3]],[3,[7,8]]]",
"[8,[[[4,6],5],[0,2]]]",
"[[[0,[6,2]],[6,[6,6]]],[[3,1],6]]",
"[1,[[6,4],[0,6]]]"
]


#Part 1, defining snail functions(adding, exploding, and splitting)
def add(s1, s2):
    return "[{},{}]".format(s1, s2)

def explode(snail):
    numbers = '1234567890'
    count = 0
    start = None
    good = False
    for i , j in enumerate(snail):
        if j == '[':
            count += 1
            start = i
        elif j == ']':
            count -= 1
        elif j == ',' and snail[i-1] in numbers and snail[i+1] in numbers and count >= 5:
            good = True
            break
    if good:
        pair = snail[start+1:]
        a = int(pair[:pair.index(',')])
        b = int(pair[pair.index(',')+1: pair.index(']')])
        left = snail[:start]
        right = pair[pair.index(']')+1:]
        newsnail = left+'0'+right
        for i in range(len(left)):
            if left[-i-1] in numbers:
                if left[-i-2] in numbers:
                    left = left[:-i-2] + str(int(left[-i-2:-i]) + a) + left[-i:]
                else:
                    left = left[:-i-1] + str(int(left[-i-1:-i]) + a) + left[-i:]
                break
        for i in range(len(right)):
            if right[i] in numbers:
                if right[i+1] in numbers:
                    right = right[:i] + str(int(right[i:i+2]) + b) + right[i+2:]
                else:
                    right = right[:i] + str(int(right[i:i+1]) + b) + right[i+1:]
                break
        return left  + '0' + right
    else:
        return

def split(snail):
    numbers = '1234567890'
    newsnail = snail
    for i in range(len(newsnail)):
        if newsnail[i] in numbers and newsnail[i+1] in numbers:
            numb = int(newsnail[i:i+2])
            newguy = None
            if numb%2:
                newguy = str([int((numb-1)/2),int((numb+1)/2)]).replace(" ", "")
            else:
                newguy = str([int(numb/2), int(numb/2)]).replace(" ", "")
            newsnail = newsnail[:i] + newguy + newsnail[i+2:]
            done = False
            return newsnail
    return


#Iterate over each snail to sum and reduce each one resulting in the final snail
snailsum = snails[0]
for snail in snails[1:]:
    snailsum = add(snailsum, snail)
    while True:
        done = True
        while True:
            exploded = explode(snailsum)
            if exploded:
                snailsum = exploded
            else:
                break
        splitted = split(snailsum)
        if splitted:
            snailsum = splitted
            done = False
        if done:
            break          

#This function calculates the magnitude for only one pair within a snail
def magfunc(snail):
    numbers = '1234567890'
    for i, j in enumerate(snail):
        if j == ',' and snail[i-1] in numbers and snail[i+1] in numbers:
            start = None
            end = None
            k = 2
            while True:
                if snail[i+k] == ']':
                    end = i+k
                    break
                k += 1
            k = 2
            while True:
                if snail[i-k] == '[':
                    start = i-k
                    break
                k += 1
            newnumb = 3*int(snail[start+1:i]) + 2*int(snail[i+1:end])
            return snail[:start] + str(newnumb) + snail[end+1:]
    return       


#This function uses magfunc to calculate the magnitude of the whole snail
def totmagfunc(snail):
    count = 0
    reducedsnail = snail
    numbers = '1234567890'
    while True:
        if ',' not in reducedsnail:
            break
        if reducedsnail[0] in numbers:
            count += int(reducedsnail[:reducedsnail.index('[')])
            reducedsnail = reducedsnail[reducedsnail.index('['):]
        mag = magfunc(reducedsnail)
        if mag:
            reducedsnail = mag
            done = False
    return int(reducedsnail)

#Print part 1 answer
print(totmagfunc(snailsum))


#Part 2, snailsuperfunc does the reduction and magnitude calculation of part 1, but for a single snail
def snailsuperfunc(snails):
    newsnail = snails
    while True:
        while True:
            exploded = explode(newsnail)
            if exploded:
                newsnail = exploded
            else:
                break
        splitted = split(newsnail)
        if splitted:
            newsnail = splitted
        else:
            break
    return totmagfunc(newsnail)

#Run superfnailfunc on each added pair of snails, both commutations as magfunc(x+y) != magfunc(y+x) when adding snails, and find the largest magnitude
biggestsnail = 0
for i in range(len(snails)-1):
    for j in range(i+1, len(snails)):
        sum1 = snailsuperfunc(add(snails[i], snails[j]))
        sum2 = snailsuperfunc(add(snails[j], snails[i]))
        if sum1 > biggestsnail:
            biggestsnail = sum1
        if sum2 > biggestsnail:
            biggestsnail = sum2

print(biggestsnail)





