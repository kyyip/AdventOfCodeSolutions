#Solution for https://adventofcode.com/2021/day/17 by Kelvin Yip

#Puzzle input
xbound = (94, 151)
ybound = (-156, -103)

#Part 1, x velocity is irrelevant just find largest y velocity that remains within y bounds
#Func to calculate y path given an initial velocity and stopping point
def yfunc(velocity, stop = 0):
    pos = 0
    path = [0]
    while pos >= stop:
        pos += velocity
        velocity -= 1
        path.append(pos)
    return path

#Any positive initial y velocity will always result in a trajectory that lands on y=0 after a number
#of steps equal to 2 times the initial velocity. On that step, y velocity with equal to the initial velocity but negative.
#The largest initial y velocity that lands within the ybounds is equal to the absolute value of the bound minus 1.
#Thus, we only need to check this one velocity and its max y value during the path
print(max(yfunc(155, -156)))


#Part 2, accounting for x velocity as well
#Idential function to yfunc except with x included
def xyfunc(xv, yv, xstop=10, ystop=0):
    path = []
    x = 0
    y = 0
    while x <= xstop and y >= ystop:
        x += xv
        y += yv
        yv -= 1
        if xv > 0:
            xv -= 1
        path.append((x,y))
    return path

#These four values which are our bounds for x velocity and y velocity were found fairly intuitively
#yvmin and xvmax are just the x and y bounds as if these values are any lower/higher repsectively
#the projectile would travel past the bounds in the first step.
#yvmax was found using part 1.
#xvmin was found by finding the minimum x velocity that would remain in the bound, solved easily using n(n+1)/2 where
#n is the initial velocity
yvmin = -156
yvmax = 155
xvmin = 14
xvmax = 151

#Iterate through the ranges of velocities specified above and increment the count whenever somewhere in the path, the projectile
#is within the xy bounds.
count = 0
for i in range(yvmin, yvmax+1):
    for j in range(xvmin, xvmax+1):
        path = xyfunc(j, i, xbound[1], ybound[0])
        if path[-2][0] >= xbound[0] and path[-2][0] <= xbound[1] and path[-2][1] >= ybound[0] and path[-2][1] <= ybound[1]:
            count += 1

print(count)



