#Solution for https://adventofcode.com/2021/day/12 by Kelvin Yip
puzzleinput = ["zi-end",
"XR-start",
"zk-zi",
"TS-zk",
"zw-vl",
"zk-zw",
"end-po",
"ws-zw",
"TS-ws",
"po-TS",
"po-YH",
"po-xk",
"zi-ws",
"zk-end",
"zi-XR",
"XR-zk",
"vl-TS",
"start-zw",
"vl-start",
"XR-zw",
"XR-vl",
"XR-ws"]


#Find what other caves are connected to each individual cave and mark big/small caves
#Messy but works
paths  = {}
bigs = []
smalls = []
for connection in puzzleinput:
    a, b = connection[:connection.index("-")], connection[connection.index("-")+1:]
    if len(a) == 2:
        if a[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if a not in bigs:
                bigs.append(a)
        elif a not in smalls:
            smalls.append(a)
    if len(b) == 2:
        if b[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if b not in bigs:
                bigs.append(b)
        elif b not in smalls:
            smalls.append(b)
    if a not in paths:
        paths[a] = [b]
    elif b not in paths[a]:
        paths[a].append(b)
    if b not in paths:
        paths[b] = [a]
    elif a not in paths[b]:
        paths[b].append(a)


#Part 1
#Use recursion to generate all possible walks from 'start' to 'end' that never visit small caves nor smart more than once
#Used list() a lot to avoid breaking things
tot = 0
def visit(smallcaves = list(smalls), path = ['start']):
    global smalls
    global tot
    if path[-1] == 'end':
        tot += 1
    else:
        for i in paths[path[-1]]:
            if i in smalls and i in smallcaves:
                newsmallcaves = list(smallcaves)
                newsmallcaves.remove(i)
                newpath=list(path)
                newpath.append(i)
                visit(newsmallcaves, newpath)
            elif i not in smalls and i != 'start':
                newpath=list(path)
                newpath.append(i)
                visit(smallcaves, newpath)
visit()
print(tot)


#Part 2
#Added an additional condition that allows for a single small cave to be visited twice, increasing the number of walks
tot2 = 0
def visit2(smallcaves = list(smalls), path = ['start'], dupes=True):
    global smalls
    global tot2
    if path[-1] == 'end':
        tot2 += 1
    else:
        for i in paths[path[-1]]:
            if i in smalls and i in smallcaves:
                newsmallcaves = list(smallcaves)
                newsmallcaves.remove(i)
                newpath=list(path)
                newpath.append(i)
                visit2(newsmallcaves, newpath, dupes)
            elif i in smalls and dupes:
                newdupes = False
                newpath=list(path)
                newpath.append(i)
                visit2(smallcaves, newpath, newdupes)
            elif i not in smalls and i != 'start':
                newpath=list(path)
                newpath.append(i)
                visit2(smallcaves, newpath, dupes)
visit2()
print(tot2)