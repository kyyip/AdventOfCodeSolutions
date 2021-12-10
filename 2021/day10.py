#Solution for https://adventofcode.com/2021/day/10 by Kelvin Yip
#Sample input used because real input bigger than Jesus
puzzleinput = ["[({(<(())[]>[[{[]{<()<>>",
"[(()[<>])]({[<{<<[]>>(",
"{([(<{}[<>[]}>{[]{[(<()>",
"(((({<>}<{<{<>}{[]{[]{}",
"[[<[([]))<([[{}[[()]]]",
"[{[{({}]{}}([{[{{{}}([]",
"{<[[]]>}<{[{[{[]{()[[[]",
"[<(<(<(<{}))><([]([]()",
"<{([([[(<>()){}]>(<<{{",
"<{([{{}}[<[[[<>{}]]]>[]]"
]


#Part 1 and part 2 all in one because this puzzle is fairly easy
syntaxscore = 0
op = ["(", "[", "{", "<"]
cl = [")", "]", "}", ">"]
points = [3, 57, 1197, 25137]
goodpoints = [1, 2, 3, 4]
autoscores = []
for line in puzzleinput:
    active = []
    good = True
    score = 0
    for i in line:
        if i in cl:
            if active[-1] != op[cl.index(i)]:
                syntaxscore += points[cl.index(i)]
                good = False
                break
            else:
                active = active[:len(active)-1]
        else:
            active.append(i)
    if good:
        for i in range(len(active)):
            score = score * 5
            score += goodpoints[op.index(active[-i-1])]
        autoscores.append(score)
autoscores.sort()
print(syntaxscore)
print(autoscores[int((len(autoscores)-1)/2)])