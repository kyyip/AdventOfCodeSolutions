#Solution to https://adventofcode.com/2021/day/20 by Kelvin Yip
alg = "#####.##....##....##.#.....##....##..########.#.##.#.#.##.#..##.#.####.######.#####.######.##..#######.#.#...#..#.####..####...#.####..#......#...#...##.#.....#....#..###.#..##....#.#....#...##.###.#.#..##.......####.........#.#.###.#.#.....#..##..##.#.##..###.##.###.#....#.#..##.#.......###..#.#.#.#.#.....#..#.###.##..##...#....##...##.##...##.#..####.#...#.####...####..#####.#####.#.##...#.###.#######.###..#..##.#.#..#.#.#######.#####.#.##.#.#...##.######.#...##.##.#.........##...##.....#.###.#.##.#.####."

image = ["..###.#.#...##.#....#..##....##.#.#......#.##.##...###..#.##...#..#......#..#....###.###..##.#..#.##",
".#...#..#.##.##....###.##.######.#.##..#..#..#.##.#.###.#..#..##...#..##...######.#..####.#.#.#..##.",
".##.#.##.#.....###.#.#...#####.#.#.#....#....##...#.....##.#...##....##.#.#.#..##.##...#..#..#..#..#",
"#.###.###.#.#.#....##.#.....#.#.#.#...#.#.#####....#.#.##.###..##..#..#.#...#.....#....#.###.#..#...",
"#.#.##..#..###..##...####.#....#.#.#.###.##..#....##.#..##.#...####.....#.#..##.##....######..##.#..",
".#..#..##..#.#.##.####..#..#..##.#.#..##.##.###....#.#.####..#.#.####..##.###...#..#.#....#..#..###.",
"..##.#####..#...##.#...#####...#.##....##.###...#.#.#.##.#.####.##..#.#.#..###...#..####......###.##",
"....#......###.#...###..#####.#.##.#.#####..####..##...#..#.####.#.##########.######...####.###.####",
"###.####.#.###.#..#.##.#.#.#.####.##...##.....#..#.###..####..#.#.#..#######..###.....#..##...#....#",
".###.#.#######.#..###.##..#.#..#..######......##.#.##..#....##...#....###.######.#.#.#.......##.....",
"#...#.####....#...#.####.##..#.#####.#..####.###.#...##....##..##.#.##..#.###.##..###..##..#.#...##.",
"..#..##.##.#..#.###.......#..###...##.###..#.##.#...##...#..####.##.######..#.#.#.#..#####.#########",
"####.##..###..###.##.#.####.##.....#.###..#..##.#...###..#.##...#...###.######.##..#..#####..#.#.###",
"######.##...##.......#.##...#.####.#.##.#.#..##.#.#.##.#...##..#.##.##.##.####.####..##...#...##.#.#",
"#.##...##...#..#.##.#.##.#####....#.##.###..#####.##.###.###..##.....#####..#...#..#.#.##.##.#.##.#.",
".##.#...#.#..###.#.##.#..#.....########...#..##..##..##..###.....##...#.#.##.###.#.#####..##..##..#.",
"#.#.#......####...#...###..##.##.#.##.#....#.#.######...##.#...#.##.##..#...####...#...##.#.####.##.",
"#..###..#.....#..###...#.#.##.######....#.#...##..######.#.###.###.......###...#.....#####.....#.###",
"#.#.##...##.###..#.###.#.##..##.##..#.#.########........#####.#.###.#.##.#.###.#..####..#.#..##..###",
"#...##...###.#.#.##.....#.##.###.#..##..#.###..#.#.##.#.##..#..#.#...#.#.#####..######.#.#.##..#.#..",
"#####.#....#.#..###.#....#.##..#.###.#.......###..######..#.##.###..######.#.##.#..######.##..##.#..",
"##...##...###.#.###.#.####...###.######...#...#########.#.....#...##.#.....#..###..#..##..#.#####...",
"#.###..#.#.#.##.....#...#.#..#...##...####..##..##.##............#...#...#..#.###..#....#.#.#.#.....",
".##..###.#...##...#...#####.##....#.#...#.##.#.##..##..#.##..#...##........#.....#...##...#..#.#.#.#",
".#.#.#.##..#...###.####.##.......##.###..#.##.#####...#.#.#####.####..####.#####...######..#.##.....",
".##...#.##..#..#...#......###....#.#..##.##..#...##.#.#..#####.#.######.####...###......#.....##...#",
"...#.#....#.#.#...###..##..#.####.#..##...##.#.##.....#...#.#.#....#.#.##.#..#....#.####...#.....###",
"##....#.####........##...#..###.#.##..##..#.....####.#.###.##.#.##....###.##.#..##.###.##..##..##..#",
"#..##.....#....###.##....#.#.....####.###..####...#.#####..#.#..##..#.##.#........#.#.#.##.###.#.##.",
"#..######.####..##...#.#...#########...#..#...###..##.###.....#.#..##.#....#..#.#.#.........#..#.#.#",
"##.....#..###.##..##..#.#..###.#.#.##.###....#.##....#.###...#.#.##.#..#.#.###.###.##....###...#.##.",
"....#####.#......#..###...##.#........##..#.#####..#.#####...#.##..##.#..#..#.#.#....#..#..#...###.#",
".###.##.##......#.###.#.#.##..##.#..#.#.#..#..#...##.##..#.########.##..##.#.#..#...####.###.##.##.#",
".#.####....#..##.#.....###.##.##..#.##...#.....#..#.......#.#..#..###.#..###..##.###..##..#.##...#..",
"#.....####.###..##.#....#####......##.#..##..##.#####....###......##.#...##.#.#...#####..#####.####.",
"..###..#..##...##.#.####...#########.###.#.#.##...#..#..##..###.##.#..###.#.#..##.....#.#..#.###.#..",
"###...#.#....##.#..#....###......#######..##.####.#.##.#.#.#..#....##.##....#..#####.##.#....####..#",
"...##.###....#..#....#.#.#...##.#.#.###.....##..#####...#.###.##....##..###.##.##.###..#.##..##.##..",
"#.######....#.###..##..#.##..###.##...##.#.###.#.#....#.#######..#...#..#.#..#...#.#..##...##.#...##",
".##.#...##.###.#..##..#....###.#..###..#....#..##..#.#....#.####.#.#.#.#########.#..###.#..#....####",
"...#.##..#####..#..##..#.##.####...###..###.#.#.#.#.##.###.######.#.#..#...###.##.#...##.#.#.#.###.#",
"#..####...#####...#.##..##..##.#####..#.#.##.#...#..#.###.##...#.#.####.##.######..#.##....########.",
"#.#.###..##.#.#..#.#..#.#########.#.#...#..##.#.#..##..#.#.###.#..#.#####.##.#.##.#.##......###.##.#",
".#.###..##.##...####.##..##..####.....#..#.....#..#...##.##.#...#..#..#....#####....#.#..#.##.##.##.",
".#.#.##...##..#.####.##..#.....##.##....###.##.....#..#.######...##..#.#...#####...#..#...#.#.###.##",
".##.##.#.##.....######.#.#.....##..##.....#...#.#.#..###.#.#.#....#.#...#..##.##.#...##.#..##..###.#",
".#.##...#.####.##..#..#.#....##.......#.#.###.##.#.####.##.#.##.#...#.#.#.#######.##....#..#.#.##..#",
"......###.#.#.##.#####..####...#...#.##....###.#####..##.##.......###..#.##..#..#..#.#..##.#...###..",
".#..#.##..#.#.##..#..#######.........##...###...#.##..##..#.###.#...#...#.##.#..#####...#..#.#######",
".#.#.#.#....##...###..###.##########.#..#.##...##.##.....#.#.....#..##.##...##.....####.##..####.#..",
".#.##....#.#....#..#.###..#.....#...#.#.#...#.#..#.#.##.##...#...###..#....#.#.#####.####.#.####.##.",
"..#.#.#..#########.##.#....#.###.##.###.#.#..###.#..####.#..#.#...###...##...##..#.##.#..######..#..",
"#.#.#.#####.######.#.##....###.#.###.###.....#.#.##.#..###..##...##.####...##.#..####.#.#.....#...##",
"#.##.#.#..###....#.##..######......#####.##.##......##.#.###.#...##......##.###.#.##...#.#.#.......#",
"#####.##....#..#####.#.###...#.###.#.##..##....#.###...#...##.###..#####...#.###.#.#.##....#.#.#..##",
"#.##.##....#..#.#...##.....###.#..###.#.###...#..#..##..##.#.#.###....#######.#.#...#...#.#.#..#.#.#",
"##.#####...#.#.........##.###..#.#..###..#.##...#...#.##..#.##......#...#.#..#..#..#..#.....##.....#",
".#.##..###.#..#..###...#.##.##..##.....###.#.#.#####.##.#.###................#..#.##..##....#.#.###.",
".....##.....####...#.####......#....#.####.#####.###.#..###.....#....####.####..#.##..###.##..#.....",
".#..###.#..####...#..#..##.###....#.#.#..#...#.###.#...#..#..#.#..#.#...#...#.###...#.##...###.####.",
"#.###....#..#...#..#.#...##.#..##....#.#######.#...###.##.#.#...#.....##.##....####.#..####.##.##.#.",
".##.#.###.#..#.###..#.##..#.....##..##....##...#########.#.###....###....##....##...#..#......#...#.",
"######.##.###.####..####...##........###.#.#...###.##..#.#....#.......##..##..#.....#.##......#...#.",
"....##..#.##...##....##.#...##.##..#####..######.#...###.####.#####..##...#.#.##.#........#.##.##.##",
"#####..#.#..#########...#####..#..#...###..##.###..##..#....#...####.#.##.#..#.##.....#..#...###...#",
".#.....##....##.....##..####...#..#........#.....##.###.##.#....#.#.###..#..#.#...##.##.#.###.##.#..",
"#####...###.###.#.#######...##.#....#....#....#...##..##...#...#.#..###.#...#.##.....#.#..##.#.##.#.",
"#####....#..###..#.#....###.####.....######....######.##....#.###..###.####..#...###.#..#.########..",
"###......#.#...#.#.##.#.#.#..###..#.####...#.###..#.###.##.#...#..#..##..##.######..#..#.##.#.#####.",
"...#...#####...#.########.#.#####.......###...###.#.##.##.#...######..#.#..##.#....#..#..#.##...#..#",
"####........#..##..#......##...#.#.##..#.##.#.####...#.####.##.##.#.#..##..#....#...##......#..##.#.",
".######...#.###..####....#.#....##.......#.#.....####.....##.#####.##.#..#.#.###..#.#.#.#..#..###.##",
"#..#.#.#.#..#.##....#.##.#.###....##.#..###.#...#.###...#..####.##.....#.#####.####...#.##.#.#####.#",
"..#####..#...#..#.#.##.#...###...#.......#....#..#..##..###.#####..#.#..#...###.#.#.##.....##...##..",
"##.#.#...##...###......#..#..##..###..##......#..#.##.##..##...#..#.#.#.#####.#..#..##.##.##..##.#..",
"#.##...#...#...###..#.##..##....#....###..#...#.###.#..##...###.##.#.#..##..####.####..##.##.##.##.#",
"#...#######.###.##....#..###.#.#......#.####..#..##..#.#.###...#....###.....#.#....#.#.##.....#.##.#",
"..#.##...#.#....##....#..#####..##.#.#########...#.##.##.###..##...##..#...###..###...#...##....#.#.",
"#.#.###.##....#.#.###.....#..#.##.#...##.####...###.......#.####.#.#..##...###.....##.#.####..##.##.",
".#####.###.#.##..#...#....#..##..##.##.##.####...#......##.#.#..#.....#.#..##...####.##..#.##.##....",
"....##.#..#....#....##..#.##...#..#...###..#..########.#..#..#..####..#.###.#####..###.##.#...#..###",
".####...###.#...#.#.#.#.#..#.###.#.#.#..#.##..#....#####..#..#..#.......#..#..####.##.#.#..##.####.#",
".#.#.###...#..###.#..##.##..#..#..#..###..#.####..###..#.#.....#.#.#.#.##...#..##..##..#........#.#.",
"#.##.#.....#.......##.##...#.##...##.#.#.#..#.#####.#.##.##.#...####.#..#....#.##.###....#.....##.#.",
"##..##.#..#..#.##..##.##.###.#....#..#...#.##.#...##.####.#.#..##...##.#...#..#..###...##..#.#......",
".......#...#.####..#...###.#.##.##..##.#.##..##.##.###..#...##..#.###.##....#.#.#..#.#######.......#",
"....#####.###.#.#..#.##.####..#...####...###..#..####......###..####.###..#...#.#.##....##......##..",
"#.##.#.#.##..#.#....##.###...#..##..#.#..####.....####.#######.#..#..######.#.#...#.####......#.##.#",
".#.#.###..#.##..#.#.###.###..#..#...#.#.#.##..##..#..#..#..#........##..#.##..#.#....#..#....##..#..",
".#...##..#..#..###.#####.#.##.##..#.#.#####........##..#..#....###....####..#.##..####.#.#######.#..",
"#..#.####.###....###....####.....#.#.###..##..#.######.#.....#..#.##.#..#.#.######....#...#####....#",
"#...#.#.#.....###..#.#..#.######....#.##..#.#.#.##.##.##.......#...##..###.#.##..###.###.##..#####.#",
"#..###.###.#..##...#.####.#.########.###.#####.##.##.####..#..######...##..#.....#.##..#..#....#...#",
"###..###.##.#...###.#..##....##.#..#.##..#........##..##.#..#.#..#.#...##..#...#.###.#.#.#..#.##....",
"..#.##.....#.#####.#.#..#......##.##.##.#.##.####.#..#..#.##..##.###.#.###.##...#....#..##.###..#.#.",
".##..#..#..#..##.##.#..##.#..##.#...##...#.##........##........#.#..###.###..###.##.#...##.####.#.##",
".#.########....#.....#....##...#...#.##.#....##.#.#....##.#..#.###.#####......#...####.####..###.##.",
"...#..#.##.##.......#.......###.##.##..###.#.#....##.##.#.#....#.##.....#....##.....#.#...#...##..#.",
"####..#.......#..##...#..#...########.##...####..###.###..##.#.###.#..##.###.#..##.#.#...#..##..#.#.",
"...##...#.###.#.....#..#.###..#...###.###.#.######.####.#...##.##.###.##.....#.##..##.#.####..###.#."]

#Part 1
#Function for focusing an image
def focus(n, alg):
    tot = 0
    for i in range(len(n)):
        tot += int(n[-i-1])*2**i
    return alg[tot]


#As we need to account for pixels outside of the image, we can use this border function to do make our lives easier
def border(image, pixel = '.'):
    dim = len(image)
    return [pixel*(dim+6) for i in range(3)] + [pixel*3 + row + pixel*3 for row in image] + [pixel*(dim+6) for i in range(3)]


#Function to generate a new image
def newimage(image, alg, pixel):
    bigimage = border(image, pixel)
    dim = len(bigimage)
    output = ["" for i in range(dim)]
    for i in range(dim):
        for j in range(dim):
            area = None
            if i == 0 or i == dim-1 or j == 0 or j == dim-1:
                if bigimage[i][j] == '.':
                    output[i] += alg[0]
                else:
                    output[i] += focus('111111111', alg)
            else:
                area = [bigimage[i-1][j-1:j+2],bigimage[i][j-1:j+2],bigimage[i+1][j-1:j+2]]
                numb = ""
                for row in area:
                    for guy in row:
                        if guy == '.':
                            numb += '0'
                        else:
                            numb += '1'
                output[i] += focus(numb, alg)
    return output


#Run it twice
image2 = newimage(image, alg, '.')
image3 = newimage(image2, alg, '#')

#Count lit up pixels
count = 0
for row in image3:
    count += row.count('#')
print(count)


#Part 2, same thing but 50 times
#This can be a lot more optimized if you don't unnecessarily expand the border each iteration like I am, but it still works given a couple seconds
focusboi = image
for i in range(50):
    pixel = '.'
    if i%2:
        pixel = '#'
    focusboi = newimage(focusboi, alg, pixel)

count =  0
for i in focusboi:
    count += i.count('#')
print(count)

