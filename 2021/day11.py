#Solution for https://adventofcode.com/2021/day/11 by Kelvin Yip
puzzleinput = ["4836484555",
"4663841772",
"3512484556",
"1481547572",
"7741183422",
"8683222882",
"4215244233",
"1544712171",
"5725855786",
"1717382281"]

#Merged both part 1 and part 2, answer to part 1 given by reading "Total Flashes" in printed output at step 100
octopi = [[int(i) for i in row] for row in puzzleinput]
times = 0 
steps = 0

while True:
    steps += 1
    #Start by adding 1 to every octopus
    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            octopi[i][j] += 1
    #Check for flashing octopi through individual rounds
    flashing = True
    while flashing:
        flashing = False
        flashers = []
        #Check for any octopus greater than 9, set them to 0, 
        #and append them to flashers to check for adjacent octopus later.
        #If any are found to be flashing, this part of the code repeats until there are no more remaining flashing octopi
        for i in range(len(octopi)):
            for j in range(len(octopi[i])):
                if octopi[i][j] > 9:
                    flashing = True
                    octopi[i][j] = 0
                    flashers.append([i,j])
        #Add to total flashes
        times += len(flashers)
        #For each octopus in flashers, add 1 to every adjacent octopus that also isn't 0 i.e. already flashed
        for guy in flashers:
            adjacent = []
            for k in [-1,0,1]:
                for j in [-1,0,1]:
                    if guy[0]+k >= 0 and guy[0]+k < 10 and guy[1]+j >= 0 and guy[1]+j < 10:
                        adjacent.append([guy[0]+k, guy[1]+j])
            adjacent.remove(guy)
            for adj in adjacent:
                if octopi[adj[0]][adj[1]] > 0:
                    octopi[adj[0]][adj[1]] += 1
    #Simple check for round when all octopi have flashed
    bright = True
    for row in octopi:
        done = False
        for guy in row:
            if guy != 0:
                bright = False
                done = True
                break
        if done:
            break
    print("Step {}".format(steps))

    for i in octopi:
        print(i)

    print("Total Flashes: {} \n".format(times))
    
    if bright:
        break