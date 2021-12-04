#Solution for https://adventofcode.com/2021/day/4 by Kelvin Yip
#Sample input used, real input is 100 boards lol.
winningnumbers = [7,47,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

boards = ["",
"22 13 17 11  0",
" 8  2 23  4 24",
"21  9 14 16  7",
" 6 10  3 18  5",
" 1 12 20 15 19",
"",
" 3 15  0  2 22",
" 9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
" 2  0 12  3  7"]


#Reformatting boards and winning numbers
newboards = []

while "" in boards:
    boards.remove("")

for i in range(0, len(boards), 5):
    rows = [row.split() for row in boards[i:i+5]]
    cols = []
    for i in range(5):
        col = []
        for row in rows:
            col.append(row[i])
        cols.append(col)
    rc = rows + cols
    for i in range(len(rc)):
        rc[i] = set(rc[i])
    newboards.append(rc)
    
for i, guy in enumerate(winningnumbers):
    winningnumbers[i] = str(guy)
    
    
#Part 1
finalboard = None
numbers = None
finalguy = None
#Check for winning board, and return the winning board, called numbers, and final winning number
for i in range(4, len(winningnumbers)):
    t1 = False
    for board in newboards:
        t2 = False
        for guy in board:
            if guy.issubset(set(winningnumbers[:i])):
                numbers = set(winningnumbers[:i])
                finalboard = board
                finalguy = winningnumbers[i-1]
                t2 = True
                break
        if t2:
            t1 = True
            break
    if t1:
        break
#Calculate difference of set of numbers in board and set of winning numbers
boardset = finalboard[0] | finalboard[1] | finalboard[2] | finalboard[3] | finalboard[4]
diff = list(boardset.difference(numbers))
#Turn everything back into 
print(sum([int(guy) for guy in diff]) * int(finalguy))

#Part 2
#Copied the same code as before but changed break condition and returns the last winning board instead
#Reusing variables because lazy
winners = [i for i in range(len(newboards))]
for i in range(4, len(winningnumbers)):
    t1 = False
    for j in range(len(newboards)):
        t2 = False
        for guy in newboards[j]:
            if guy.issubset(set(winningnumbers[:i])):
                if len(winners) == 1 and j == winners[0]:
                    numbers = set(winningnumbers[:i])
                    finalboard = newboards[winners[0]]
                    finalguy = winningnumbers[i-1]
                    t2 = True
                    break
                if j in winners:
                    winners.remove(j)
        if t2:
            t1 = True
            break
    if t1:
        break
boardset = finalboard[0] | finalboard[1] | finalboard[2] | finalboard[3] | finalboard[4]
diff = list(boardset.difference(numbers))
print(sum([int(guy) for guy in diff]) * int(finalguy))



