#Solution for https://adventofcode.com/2021/day/21 by Kelvin Yip
#Part 1, very easy
p1 = 1
p2 = 2
s1 = 0
s2 = 0
r1 = 0
r2 = 0
dice = [1,2,3]
turn = True
while s1 < 1000 and s2 < 1000:
    if turn:
        p1 += sum(dice)
        if p1 > 10 and p1%10:
            p1 = p1%10
        elif not p1%10:
            p1 = 10
        s1 += p1
        r1 += 1
        for i in range(len(dice)):
            dice[i] += 3
            if dice[i] > 100:
                dice[i] = dice[i]%100
        turn = False
    else:
        p2 += sum(dice)
        if p2 > 10 and p2%10:
            p2 = p2%10
        elif not p2%10:
            p2 = 10
        s2 += p2
        r2 += 1
        for i in range(len(dice)):
            dice[i] += 3
            if dice[i] > 100:
                dice[i] = dice[i]%100
        turn = True

if s1 < s2:
    print(s1 *(r1+r2) * 3)
else:
    print(s2 *(r1+r2) * 3)


#Part 2, smart brute forcing
#Instead of generating a universe for every possible roll, generate one for each possible roll value from 3 to 9 inclusive.
#Store the rolls for each turn and at the end of each game, multiply the multiplicities of each and every roll and add the
#result to the total number of universes for the winner. 

#Finding each three roll multiplicity and storing them into a dictionary
from itertools import combinations
diracdice = [[i, j, k] for i in range(1,4) for j in range(1,4) for k in range(1, 4)]

values = {}
for i in range(3,10):
    values[i] = 0

for roll in diracdice:
    values[sum(roll)] += 1

#Function to intelligently brute force the solution, it's slow, but still less than a minute.
u1 = 0
u2 = 0
u = 0
def dice(p1=1, p2=2, s1=0, s2=0, turn=True, rolls = []):
    global u1, u2, u, diracdice, values
    u += 1
    if s1 >= 21:
        wins = 1
        for roll in rolls:
            wins = wins * values[roll] 
        u1 += wins
    elif s2 >= 21:
        wins = 1
        for roll in rolls:
            wins = wins * values[roll] 
        u2 += wins
    else:
        if turn:
            for i in range(3,10):
                newp1 = p1+i
                newrolls = list(rolls) + [i]
                if newp1 > 10:
                    newp1 = newp1%10
                dice(newp1, p2, s1+newp1, s2, turn=False, rolls = newrolls)
        else:
            for i in range(3,10):
                newrolls = list(rolls) + [i]
                newp2 = p2+i
                if newp2 > 10:
                    newp2 = newp2%10
                dice(p1, newp2, s1, s2+newp2, turn=True, rolls =newrolls)

dice(p1=1, p2=2)

if u1 > u2:
    print(u1)
else:
    print(u2)