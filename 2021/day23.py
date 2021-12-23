#"Solution" for https://adventofcode.com/2021/day/23 by Kelvin Yip
#I'll be honest, I basically solved the problem manually.
#At the very least, I did so using code.
#Part 1
#I added numbers to the sides as easy to read indexes
puzzleinput = ["#############",
"#...........#1",
"###A#C#B#D###2",
"  #B#A#D#C#3",
"  #3#5#7#9#4",]
frogs = [[i for i in line] for line in puzzleinput]

ecost = {'A':1, 'B':10, 'C':100, 'D':1000}

#Function for generating Manhattan distance between two points, useful for calculating energy when moving frogs
def manhattan(p1, p2):
    tot = 0
    for i in range(len(p1)):
        tot += abs(p2[i]-p1[i])
    return tot

#I made a fun little game where you move the frogs one turn at a time and it will automatically calculate
#and sum up the energy. It also has an undo and quit option.
#As movement is done by swapping positions, the frogs can move through walls or swap positions with walls.
#It's up to the player to follow the rules as they are written in the challenge in order to get the final answer.
def game(frogs, depth = 2):
    global ecost
    energy  = 0
    last = []
    while True:
        for line in frogs:
            frog = ''
            for i in line:
                frog += i
            print(frog)
        print(energy)
        organized = True
        for i in range(2, 2+depth):
            if frogs[i][3] != 'A' or frogs[i][5] != 'B' or frogs[i][7] != 'C' or frogs[i][9] != 'D':
                organized = False
                break
        if organized:
            print('ya did it using {} energy'.format(energy))
            break
        coords = input('move a frog').split()
        try:
            if coords[0] == 'undo':
                oldcoords = last[-1][1]
                frogs[oldcoords[0]][oldcoords[1]], frogs[oldcoords[2]][oldcoords[3]] = frogs[oldcoords[2]][oldcoords[3]], frogs[oldcoords[0]][oldcoords[1]]
                energy -= last[-1][0]
                last = last[:-1]
            elif coords[0] == 'quit':
                return
            else:
                coords = [int(coord) for coord in coords]
                e = ecost[frogs[coords[0]][coords[1]]]*manhattan([coords[0], coords[1]], [coords[2], coords[3]])
                energy += e
                frogs[coords[0]][coords[1]], frogs[coords[2]][coords[3]] = frogs[coords[2]][coords[3]], frogs[coords[0]][coords[1]]
                last.append([e, coords])
        except:
            print('bad input')
 

#Play the game, minimum energy is 11332
game(frogs)


#Part 2, more manual solving lmao.
puzzleinput2 = ["#############",
"#...........#1",
"###A#C#B#D###2",
"  #D#C#B#A#3",
"  #D#B#A#C#4",
"  #B#A#D#C#5",
"  #3#5#7#9#6",
]

frogs2 = [[i for i in line] for line in puzzleinput2]
   

#Play the game again, minimum energy is 49936
game(frogs2, depth = 4)