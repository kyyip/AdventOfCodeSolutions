#Solution for https://adventofcode.com/2021/day/25 by Kelvin Yip
puzzleinput = ["v>.>>v>.v>.v.>...>>>.>>v..v>v>vv.>>>.>>..vv>>>.>>.v..v..>....v....>.v>...>..v..v.>..>>.>..v.vvv...>>>>>.v...>>>>>.>v.v>>.v>..>..>.>>..>>>>>",
"..v>v.vvv....vv.vv.v..v..>>>>...v...>..>>......v>.>.vvv.>v..>..v>...>>.......v>>.>v>.v.>>.>>v..v.v.>>>v...>v....>.>.>...v.>..>.v.v>v>v..v.v",
">vv...v.>.>.>v.vv>.>.vvv>..v...v.v.>...>.v>..v.v...vv>>.>v.>.>>....>>...>.vv...v>.v..>>..v.>vv...>v...>>...v..v.v..v>.v>v...v.v..>..>.v>v>.",
"..v>>.vvv..>>v>>.v>.....>>>.v...v..v.>......>>........vv..>.v>v.>v.v>.vv.vv>..vv>.>..v.........vv..>vv...v.>..v>.>.>>>..v.>v.v.....v.>>v.v.",
".>.v>..v.vv>..vvvvv..v..v...>v.>v..>..>>..v>.v>....>..>>...>.vv.v>.v.v>>.v>vvvvv>>v>v..>...>..vvv..>v>.v>v.v>...vv.vvvv>.vvvv...v....>>v.>v",
".v.>v..v.>.v>v>....v..>>v.>vv>.>>v>..v>..v>v.v.vv>..>v>.>.v.v.vv.v>>.vv.>..v.vv>>v.>....>.>.>v.vv...>....>..>>v.>.v.>v....v>.v>....>>v>.v..",
">>..vvvv..>v..v..v>..>.>.>...>>.>>>v.>.>.>....vv...vv.....>..>v..v.v..>>>>vv....>v.>.v..>vv...v>v...>..v>....v.v.>....>.v.>.>...v.vvv>vv>..",
".v..v..v..v..>v.>>>>...>..>......>v.v>>>.>....vv....v>>v....>.vv.>>.>v..v..>.v...vv>vv.>>>.vv>>>.>.vv.v>v.>...>...>..v>v.>>v..>..>v.>....vv",
".>.v.>.vv.v.>...>...v.v>.v.>.>>v.vv>.....>.>vv..v..>v.>v>vv.>.>.vv...v.v>.....>.>v..v..>.>v.....>..>..>..>v..>.>.v.>v.vv...vv>v..v..>.v>...",
"v...>>...vv....vv>.v.v.>>..vvv>>v...v.vv.v.v.v.>..v..>....v>vv>..>vvv>>..v>>>>.>.v...v>..>v.v.>..>v..>v>vvvvvv.v....v.>...>.v.v....vv>...v.",
"v........>v.>..v..>...v.v>.>.v.v...vvv>...>..>v.vv.....>>.>>>..v.....v>..>.v.>v>vv>.>vv..v.v>.v....v>...v.>>>>...v.v>>..v...v.vv.vvv...v..>",
"v>.>.v>v.v.v>>v.....>..v.v>.v.v.>..>v>vv...v.v.>>vvvvvv.v..vv......>v>v.vv>.>v.>..v>vvv.>>v.v>.>.>.v...v...v.>.vv..>.>vv.vv.>>>>>v.>v.....>",
"v..v.>v>vvv..>.>..>.>>....v>.vvvvv..>..v..>>..v>..>>>vv..>>.v.>......v..v.v.>..>>v...vv>>.v..>..>v>v..v..v>.>.>.v.>...>>>...v........>.>v>v",
"v.>v>.....vv..>vvv>>.>.v.>v.>v.vvv.>>>>.....>...v...>...v.....v..v.v....v>.>>v..v>.>.v..v.......>v...v.>..v..>.>.>>>...vvv>..v>>.vv>.v.>..v",
"v..>.v.v..v...v.>.>.>.>.v...>.v>.v.v>...vv.>.v.....>....>....>v>......>.>..v..v.>...v.>..v...>>>.>>....>.v>.v>v>v>>.v>.v>v>..v.v.v..>>.....",
"v>.v>.>>>>....v.>.v......>>v.>vv..v.>..>.....>.v>....>.v.vv>v>.>v.>.>>vvvv.vv.v>.>.......>...>>.v>vv.v..>v>...>.vv..vv>v>..vvv>...>......>v",
".>>v..>>..v..v..>...v.>v.>.>.v......>..>...>v.>.vv>...>vv>v..v..vvv.>v>..v..v>>.>>.v..>..>>>...vvv..vv.>.v.vvv>...v>>.v.>..>vvv>.v.v..v....",
"v..>...v.vv>vv.>>v>>.>.v....vv>vv..v>.>.....vvv..>.>...vv.vvv.vvvv.v>.>...>..>v..>....>...v..vv>>v>>......v..>..>.>vv...v>...>..v.........v",
"..........v...>.....v..>..>>.>>.....>...>..>.vv>.>.vv..>v.v...>>.vvv...v..v>..>v>..>.>vv>>v...>.v.>.>>.v.....vvv>...v>vv.>vv>>.v>...>.>v..v",
"..>.vvv..>.vv..vv>vv.>...v>>.v..>.vv.>>v>v>v.v.>v>..>>.>.vv..v>.v....v.v.>v....vvv.vv.>v>..>.vv>.>.vv.>.>.>v..>>.v.v.>>.v....>.>>>v.>v.>.vv",
"v>v.>>.>>.>.>.>.v>.v>..>.v>v>>>vv.>vv...>>.>>vv>...v.vvv..>.>v..v..v.vv>v.v..>...>.v.vv....>.......>.v..>....>..>v......v........>>vv.v.>..",
"....v.>vvv...>v..>...>v.v>>.vv.v..>>>..>v.>v.vv.>..>v>.....v.>>...>..v>>.v>>>.....>.v..>v.v...>v.v>>>>..v>>>v.v>v..v>vv..>..>v>..v.>v>v.>>v",
".>...>..>>>v.v...>v..>.v..vv..>....>....v..>vvv.>.v..v>v.v.>vv...v>v...v.>..v>v..v..vv>>vv.....>.v>>...vv...v...>.>vv.v>..>v>vv....v.....v.",
"...v>v>v>v.>..>..v.>..>..v..v....v..v..v>...v.>vv.>>v.>.>.v...vvv>...v>....>v...>>...v>v.>v....v>>..>v.v>.>v.v..>...>>...>>>..vv.>..v.>..>.",
".vv>.>v..>vvv..>.>>v.>.v.>.>>vv.>..v.v.vv>v.vvvvv>.v.>........v>vvvvv....vv>.v...v.>....>v......>>.>.>>v.>>..v.........>v.v.>....>....>>v.v",
">>.v.v.>v.v>.>.v>..>vv..v.>v.>>>..>.v>.>.>.v.>>>v>...>vv>.vv>...>>v.v>.v..v.....v.v........v.>.>>..vv.v>.v...vv>vvv>v...v...v>>vv.>.v..>>..",
"vv.v>.v>v>>>>.........>.v>..v>....vv>.v>..v..v..>.v>.v..>>..>>..v.......vv>>>v.v..>..>>v>..v...>.v..vvv.>vv.vvvv>>.v.v...v.>...v.v>>v>.>vv>",
"v......v...>.v>v....v..v.>..v>>.>.>vv.vv.vv>v.>.v>v>v>v>>..>vv>vv..v..v.>..>>.vv>v..>>v.v>v.vvv>.....>>..v>>v......>>>.>vv>.>vv...>>..vv...",
"v..vv.>....v..v......>.v.v...>v.v.v.>..v>.>.v.v.>>>.>>>.>..>.v..v.v>..v.vv.v.>vv>>v>v.v>v....>v...>..v.v..v..>..>.v.>v.>>..>vv..vv..v>>>>v.",
"v...>>v..vv>.vv...v.v>>>vv>v.v.....>...>v.v>..v.vv..>>>v..>>v.>vv>.v>...v.v.v....vv>>vv>....vv.>v.v.v.>..>..>.>v>..v>...vv>v.>v>>..>>>>.v.v",
"..v..v.v..v.v>...v>v.>>.>>>v>v...vv>....v...>v...>.>>....v>v...vvv.v>...>v.....>v...>v>..>>>v.>.>.........v>..>>>>>....v..v..v...v.vvvvv>>>",
".>v...v......>v.>v.v>v>...>v>.v>>.>.>..v..>v.>v>....>>v....v.v..v>..vvv.v>.v>...>.v>.vv.vv....v...vv>>.>.>..>.>....>..>>>v.>vv>.>>..>>...v.",
"..vv.>...>.v>.>>vvvv.v.v>>..>.>>v...>...v.....v.vvv.>>>vv...>...>..>.v.v.v....v.v.>..>vv>...vvvv..>v>>.>.vvv>..vv>>v....v>...>..v...v.vv...",
"..v...v...>>>..v..v.v>..v...>>.>v....>.v>>.>>v....vvv..vv.>>..>..vv.v.>>v>>>v...vv...>v..v.v.v.>.>v.>.v.vvv>v..v....vv..>...v..>vvv......v.",
">.v.>v>vv>....>..v>..>..v.>....>.v.>>v.v....v.>v...v>>...>v......v>>v....vv..v>...v.v>vvv.v.vv.>.>>..>..v.>.>>>.v>>..v>v>>v>>v>>>>.>..>v...",
"vv....>>v>v...>v.>v>.vv>vvv>v..>.>.vvv.....>v..>...v.>>......v>.>>..>..vv.>v.>v..v..v...v>>v.>.....>....>vv.>>>>>>.>>>.v.v....v.v>v..v>v.vv",
">v.>.>.vv.vv>.>.v>v..v.>........v>>>...vv..vv...vv...>.>vvv>.v>v>vv>.>v>.>.v>v>>.>..v.v.>>>>>..v>>vv.>.>..vv>v..>>v.v>..>..>...>v>.>.vv>>..",
"v..v..v..>......>>>v..>.v........vvv>v>v.>>v.v>....>..>.>>.v..v.>v.>v>v....v>v.>.v.>.>.>..vv>..>..v.v>..vv.v.>..v......v>>.v>....vv.>>>vv>.",
"....v..v.>vv>.>.v....vv>..v.>v..v..>.v.vv.>...>..>.v.v.vvvv.>v>..v>.>v.>>....v....>>>...v..v.v......>.>vv>.v>..vvv.>.>v>.>.>vv..>.vv.vv.v.>",
">......>vv.vv..vv..v.vv.>>>v..>v.>.v..v..>.>.>>.v>..>>...vv>>...>.v.v.v>.>vv.>.v.v>.>.>>>..>>...>v....v.vvv.vvv...>>>v>>v..vvv.>>>>v>...v>>",
".v>>.>.>v.>..v.>>.vv.v..>.....>.>v>vv..v.v....>v>..v>....>.vvv.>.>v....>vvvvv>>......>vvv...>.v.........>..v..v.>>vv...v.v......vvv.vv>.>v.",
">...>v>.>v.>..v.v>..v>v..v.v.....>v>..v...>..>v.v..v.>vv..>.>v.vv.>>>..>.>v>vv>>v.>..>>.v>.>v....v.>>>>v>>>>>v.v>>>...vvv..>....v..vvv....v",
".vv.>..>.....v.....>.v>v>.v.....>....vv.v..>>>vv..>.v......>vv>v.v>..v..>>>.vv>.vvv..>v>>.v..>..>..>>.....v>>....>..v.v>.v..vv.vv.v>v...v..",
".>v......>.>vv>..>.v.>.>v....v>...v..>..v>.>.v.v.v.v>>>v>.vv.>.v.v.>>>...>....>..>..>vv>>.>...v.>>.v>.v.v.v.>.....v.vv>..v>.vv.....>...v>v>",
"..v.>.v>v..>.>.>....v..>.v..>.v>.vv>>.>>..>>v>.v..>..>.>.v.>>.>v>v.vv..>..>..>>.>>.v.>>..v..>v.......v.>>..v>.>..v>.v>>..vv...>..v...v>>vvv",
".>..>.v..v.vv>>....v...>>v>>...v..v.>...>v..v...>.v>>......>.>v.>...v..v...>v.v>......v....>>.....>..v.>>.v.v.v.>.>>>...vv......v>...>.vv>.",
".v.>v.>.>..>v>..>.vv.>.v...>>.v.>....>>v>......>.>v.v.v.vv..>>v.v.>>.v.>v>>.v>.>...>..>.v>..>..v....>...vv.v.>>........v>>.......>>.vv>..v>",
".v>v.>v>..v..>v.>.vv.>v>>v>>....vv>....>>>>.>.>>v..>v...v>>......vv>v.>vv.vv..>.v.>...>>.>vv>.>..>.....v.v.v..vv....v>..vv>>v..>vv.....>vvv",
".v>v...vv.>v......>....v>>..v>.vv...vv>..>.>v>..>.>..vv>>...>vvv.>..>..vv.v...v.vv>v.>>>>v.....v.v>..v....>...>.v>.vv.vv.>>.>...v..>vv>.>>v",
".>.v>>v..v.v.v..v.>....>.v>v.v...vv.>.>v..>v>>v.v.v>.>v>.>v..>.>.>v.v>vv>>.....>v....v>>>vv.v>>..v.>.>>>...>vv>v.v..v>....vv>>.>>>.......vv",
".>.v>.vvv.v.vv....>..vvv.>..vv.v>..v>.>vvvvvv..vv..v.v>>...v...v.v....>>>>>>.>....vv>v.v.........>vvv.v>>>.v>.vv>>..v...>.v...>v>v>.v....v>",
">.v>v.v>...v.v.vv.>>>.vv.vv>.>....v>.vvvv.....v.>.....>....>..vv>v..v....v.v.>.>.v...v.vv>...>v.>>..v...vvv...v..v.....>vv....v>v.v...v>>vv",
"v.>v........>....>v>v.v..v......>...v..v.>v.v..>.>vv>v...>>>.v>.>..>v>..v..>v...v>.v.>.v..>v>.....>>v.>.>v.v..v.......>.>.>...>v.v.v.v.vvv.",
".>...>....>...v>..v...v>v>>..v>>>.>.>>v>vv.>>vv>.>v..>.>.>>v>>vv.v.v..v..vv.v..>.>..v>vv...vv>..>...>v.vv>>...>.>..>..v>...v>>v>.v>...v....",
"v>>vvv..v...v....>..>...v>.>vv....>..v...>>....v.>.>.>.v....vvv.vvvv>.>..>v>..>.....>vv.vvv.>>>...v.>.vv.v.v>>...vv>...v...v.vv.v.v.>>v..>.",
"vv.vvv>.vv>..v..>v>..>..v...v>vv.>....v.....>.>...vv.>vv>.>>.vv..>v>>...>.>>>v.vv>......>.>.v>v>>..vv..vv.>>v>>....>.vvv>v>>...>>.>.>>.v>v.",
"...>vv.>..>..>..v.v.v>.vvv..>v>....>.v>>..>vvv.>v.v.>.v....vv.>....v>>>v>>.>v.>.>v>>.v..>v>....vv.vv>.v.>....v..>>v..>vv>.v.>>..>........v>",
">.>.>vv>v..vv.>..vv..>vv..v..v.v>.v.>.>>vv..>v....>..>v>>..v.>>>vv....v>v>>>..v.v>>v>.....>>>.v...v>.v>.v>v..>>vvv..vv.vv.>vv..v..>.>v.....",
">.v>.v.vv>.>...v>...>.vv..v.>v...v>.vv.>...>.v..>v.>.......vv...>vvv.vv.>.v..v.v..>v>>.v>>.>v.>..v.>....>..v>v....>>....v..>.vv...>v..>>...",
"..>..v>>..v>vv.>.v>.v>..>.vv.v>....v...>>.>vv>v......v....>.>.>>..v.vv>.>v.>>>..>....>..v>>...>..>..v.vv.v.vv.v..>...>>..vv...v...>.v>....>",
".>..>v.>.>v.v..>...v..v..>v>...v..>v..>vv.>.v.>v>..v...>>v>v...>>>>.vv>>.>v>.v>.>.v.v.>vvvv.>>..v...vv>.>...v.vvv>.>>..v.v>.v>v....>.v..v.>",
"v>>>.>.v.v..v>.>....>>.>>>>>v>..>>>.vv>v.v.vvvv.>>>v>>>>v>...>.>.>.vv.v...>vvv..>.v.v..>.v>..vv>>v.>.......>.vvv>vv>v.v>v>>v.>....>vv>...>v",
"..>..v....v..vv..v..v.vv..>>>.>..v>>..>.>vvv.v..v..v.>..v>........>.v.v.>>>......>..v>>>.>v>.>vv..>v>v......vv>>>>.>v.>v.v>.>v.>.>.....vv..",
">.>.>v>>.v.v.>..v>>.>v...>...v.>..v>....>vv.>>..>...vv>...>..>v.v.v.vv>.>v.>.>.v.......>>>v>>...>..>v>>vv>.>.>v>v.>...v..>>..>v>>v..v..vv>.",
".>vv>v.>>...vv..>v..v>>>v.v.....v>.....v.>>.......>..v.v>...>vv...>.vvv.v>..>v....>.>..>...>..v.......v.v....>>...>..>....v.vv..vv.v.>..>.>",
"v.......>...v.>vv......>..>v>vvv>...>vv.>v>>.>v.>.>...>.....>....>.....v>.>.....>>v.>>>..>.>..>.>..>v>.vv..v.v...>>>.>.vv.>>>v...v...vv>..>",
"..>.v.v.v......v.>>>v.>..>v>>.>>v....>vv....v>.v.vv.v...>v>v...v.v>>.v..>>.>.>.>>v>v>>.>....v>..>..>.v>vv..>....>....v.v...v>..>>>>v....v>.",
".vv.>..>.>>>v.>.v>...>..>>v.>........>>>>.>.>v.v.>...v..>..>v....v..v>....v.....v.v.vvv..>v.v>....vvv...v.>..vvv...v.>>v.>..>>>>.>..v>.>..>",
"vv.>...>v.v>v.>>...v.>vv..>.v...>.>>>v.>.v...v...v.v.v..v.v>.>.vv>.>v....v...>..>v>v>.v..vv.>..vv.>...>vvv.vv....v.v>>..v.>.>v..v..>.>.v>.v",
">..>v..>v>vv>v..vvvvvv.>>.>...>...>v....>....>>>>>.v.v.....>v.vv>>>v..v..v.vvv..>v.>vvvv..>v>...>vv.v.>.>.>>>.vv.>>>.vv.>v..vv>>v.vvv.>v>>.",
".vv>..>>>..v.>...v>vvvv.v.>vv....v...vvv..v>..v.vvvv>>.v.v.>>.>.v.>>..v.v..>..>>>.vv...>.>vv.v>>v..>..v.vv.>vv...>v.vv>..>v.>..>vv>.>....v>",
"v.>>...>.v>>......v.....v.v.>v.vv>>>...vv.>>v.>.>..>>...>..>.....>....>.v.v.v.>>vv..>>..>...>v.>..>>>.....>>v>>v>..>.v....v......>vv...v.vv",
".......>...vv.vv.>..>v.vv>....>>vvvvv>>...vv...v.vv...v>vvv.v>.>>...>>v>..v.....>.>....v......v.v.>...v......>>>...>v>>>.........>..v.vv.v.",
"v.>......v.>v...>.v..vv.v.>.>.>>>...v.v>>...>.>>>>..v.vvv...v..>>vv>.>v>...>....v>>>v...v...vvv..>.>......v>.......>.v.>v..v.vv....v.v.....",
"vv..v..v...vv>.>.v.v....v...v..v.vv.v..vvvv..v.>>v.v...>..vvvv.vvv>.v>v>vv...v>.....>.>v>>..v....>.>.v.v.v>vv..>>>v>...vvv>>vvv>.>..v....>.",
"vv>.>..>>....v>....v>v..>..>..v.>v....>>>..>...>...>.vv.v>.v.v....>v>>.>......>v..>..>v....>v>v.....>>v.v.>v..vv.>....v.>...>.>v>v.......v>",
">....>>...>>..>.v.>v..v>v>>.>>.>>.v>>>vvv..>.>.vv..vv...>..>>.....>...>.v..>.>v..v...>>>>.>v..v.>..>.....vvv..>.vv.v.v...>>v.>..v>v..>>v...",
".v.>vv>.>.v.>.v.v..>.>>.>vv>v>.>...v..vv>>v.vv.v......vvv>...>.v>.>.v..>v..>.>>>.>..v.v.v..>.....v.vv>.v>v>..>vv>>>......>v.vv>.....>.v.>>v",
"....>....>.v.v.>>vv>.vv.>v.v..>>>.>..v.>>v..>v.>>..>...v>.>>>..>....v.>..vv>.>.v..v..v>.v>>.v.>..v>v....v>v..>...>v.>v.>....vv.>.vv>.>..>>>",
"v...v>>.v>>...vvv>...v>...v>vvv.v.vv.>vvv...vv.>>>v..vv>...v>>.>v.>>.....vv.>>.v>v....>........v..>...v.v.v>v>.v>v....v>..>v.v.>..v.>..>.>.",
".vvv>..>.>vv..v...>..>..v.>>..>..>.>v>.....>.v>>>.>.v..>..>.>v..>..v>>.>.....>v....>>.v.....v>..>vv.....v.>.>.>>v.>.vv>...v.>>>.v.>vv...>v.",
"..v.>..vv>>>vv>>.v.>.>..v....vv>v..v......>v...v..>.vv...>>....v...>>v..v..v>v..v.>.>..>>>..v..v..v.>>>>.>.>.>.>.vv.....>vvv>v..>v...>.v>v.",
"..>.v>..vvv..>..v>v.v.v.v.v>.>.>..v>...>v.>>>>>v..vv.v>.>.>>.v....>..vv...>v.....v>..>>>>...v>..vv......v>vvv>>>v.v..>>.v.>..>..>..v..vv>vv",
">>..>..>vv...>>....>.>v..v..>..v>vv..>.>>>.....>...>.vvv.v>v..vvv.>.vv>...>vvv..>v.>.>>..v>.....v.v.vvv.vvv..>v..v>>...>.vv..v>>.v>v.>...>.",
"v..>>...vv..>.>.>>.vv..v>>.>.v....>..vvv>>..>v..v>..>v....>v.>v...>...v.>>>.>vv..>vvv>v.>>.v..>..>>.>.v>.v....v.....>>vvv.vv>vvv...>>.>v..v",
"....>>>.>.>v..>>..>>...v>>...v.>vv...>v..v.v>v>vvvv.v>.>>...>>.v.>.vv.>>v>..v.>v>>.vv>........v...>..v>vv.>>.v.>..>..>..>.>.v..>v...>...v>v",
">v.v>v.v...>vvv>.........vv..v>v.>>...v>.>>vv>.v.v.>v..vv..v.v.>.v.>.v..v>.>>..>.>..v>>vv.v.>v..>..>>v.>>>v>...v..v........>..v......v..v.>",
".>....v>.>>.>v.>....>v.v.>.v>.>v>>v.v.>.>>vv.>v....>.>>>>>>...>..v..v.>v.>v.v>v.>.vvv..>>.vv.>...v>.v>>.v.>.....>.v.v.....>.....>>.v.v...>.",
".>>......>>>>.>>...>.....v.v.>..>>v>.>v...>..v>....>>.....vvv>>....>..>>...>v..>v>.>>...v....>v>...v>>.vvv.>vv...v..v.>>vv>.v>>....>..v....",
">...v..>.v.vv..>...>vv...>>..v>.vvv..v..v.v.vv>vvvv..>v.>.v>>.v>>>>>.>v>>v>.vv>>>v....vvv>v..>.>..>.>.>.vv.v>v.>.vv...vv.v.v.>>.>....v.v>.v",
"v...v.v.>.>>.>>v.v>..>..v>.....>..v..>v>...v.v.>.>..vv.>.v>v>v.>>v>vv>..>>v..v..v..v..v.vv..v.vv>vv...vv>v.>>v>...>>>....>vv>>v>.>v.v>.>.v>",
".vvv>>.v.>vv.v......>vvvv.v.>v..>>.>...>v..>>v..vv..v...>>..v.>..v>>v>..>vv...>.v.vvv..>.>>>>v..v.....v>v>..>.v.v.v>>>>>v.v.>vv>>.v.>.>....",
">v>.>v..>>.>.v.v.v>.>.....v...v>.>>.>vvv.>.>>.>>vv>>..v.v..vv>..>.....>...>v.vv>.>....>......>>.....v..>>v.>vv...vv.>v..>>vvvv.>>vvvv..v.vv",
">..>..>..>v.vvv...vv>v.>v>v..vvvv.>>.>..v.v.v>>.v.v.v.>vvv......vv>>.>...>.vvv.>v.>vvv>.v..>>.v>vv.vv....>.....>..v>..v.v.>>....v..v>v>.v>v",
">...>....vv>.>v>>..v..>v..>>>....vv>vvv>..>..v>..vv..vvvv.vvvv.>.>v>>..>....v.v..v..>v...>.v>>.v..v.v....>v..v>..v>vvvv..>...>>>>.>v..>>...",
"v>..vv....v>>>.v..vv>...v.>>..v..vv>vv>...>.v>...>>..>vv..>.>.>v.>.v...v.v>>v.>.>v>..>..>>vv>>>.>....>...vvv>v....v.v.vv.>>.>.>v..>.v.>vv..",
"v>.>.>>...>>>>v...v.>v>v>v>..vv.>>...>v.v.>.v>>.>vv.vvv.v.v.v>.>>v.v.>.vv>.>v>v.v...v.>>v>>v>>v>.v..>>....>>>>vv......vv>>.>vvv....>.vv..v>",
"vvv..>..v>>..v.vv>v...vv..>vv>>v..>.v.v...v...>.>.>..>.vv.v.vvv>v>.>vv>v.vvv.v>>..>v...v>>>>v>v..>v..>.v>.v>..>>.>vv>v>>.v>v>v.>.>.....>.v.",
".>>....vv.>>>>.v..>>>>.v.>.>>...>v.>..>....vv>..>>v......>....>..>>..v.v.>..>.vv>...v....vv.v..>>vv.v.>>v.>.>>....>>>>..v.>>..>.>..v>>.>.vv",
">..vv.>..>...>>...>.>>..>v.v..v...vvv..>.>.....>>.>>..vv.v>..>v.>v.v>...v>>>v>...v>>vvv>>v......v>>.v...v.....>>...>v.>v..>>>>.v....vv..>v>",
">.>v.>>>.>..v.....>>>v>.>v.>...v..>..vvv....v...>v..>.v>.v.>.v.>..v>>>>...>>...v.>.v...>.>>v.>v.>>..>v>..v..v.>v.>...v..vv.v.v...>.>.....vv",
".vv>>..>>.v>.>v...vvvvv....>>v..v.>.v>>.>>vv......>>.>>......v..>.v.v>>.vv>.v.>.v>vv.v.>.v......>>.>.v>.>vv>...vv.v...vv.v>v.>v...vvv...v..",
"..vv.>v....>vv>>.....v>vv..v>...v>v.>>vv......v...vvvv..>.>>.>>.....v......vv..v>.v.....>v..vvv.v..v>v......vv.>>>>v....vv..>.v>>....>.>v..",
".>>v>.>.>.>..>v.>v..>>>vvv>v....v.v.>...>.>..>>>..>.>v..>.v.>>v.v.>.v>..>vvv>v......vv..vv.v...>.v...>>..v...v..v....vv>.>..v.v>vv..v..v.vv",
".........>....v.>..>v..v....>.>.vvvv>.>>..v..>....v>>.....v.vv>v..v....>>...>.v..>..>..>.vv.>>>..v>>>>.v..v>>.>.v.>>.>.>v..>.vv>v>>>vvv>.v.",
".>.>.>.v..>...v........v>..v..v>>vv.>>.v...>..>....>>.vv..>v.>.v>...>v...>>.v.v>vv.v>>.>v.v>..>>.v>.>.>>..>.....v>v......v.>v>.v...>.>..>..",
"..>>v..v>>..v>..vv..>>vv>.>>>.v....v.>.>..>..>.v.v>..vvv>vv.>.>v...v>>.v>...>.>v>v.v.>..v.>>vv>..........vv..v>.>v...>>.v>>>..>..>>.>v>..v.",
".....>..>..>..>v.vv>.v>.vv>...>>>.>..>>>..>>vvv.>.>..vv....>v.>..v...>>>v.>.vv.>.v.v...v...>>..v>v...v...v.vv.>.>.>.>v>.>v>v..vv..vvv>>>.v.",
"v...>.v.....>.v>..vv.vv.vv...v>.>...>>.>v..>>vv.v.v...vv.....v>.>vv>vv.>>.vvv>..>..>>......>.>vvvv.>v.vv.....>>.>>vvvv.vv>>..>...vv.>..>>..",
">>v.vv>.v...>v.>..v...v.v>>.>..v.>..>>.v>.>.vv>>vvv.v..v>..vv.......vv.>vv..>..>>...>vv.>...>>v.v....>.v>.>>v...>.v>.v..v..v....v>vvv....v.",
"v>v.>..v.>.v.>.v..v>>>.v.v>.>.v..v.>.>v.v...>v.v.v....v.>..>v.v>...v>.>.>v>>v.....>v...>vv.>v..>...>>>..v.v.....>>v..>.>..>.>..>>v>>v>>v...",
"...v>>>.>.v>>>..>.vv.v>....vv>vv>v....v...v.v>vv....>>vv.......>.>v>.>.>..>..vv.v>.>>.>.v...v>.>.v.>>..v>.v>.>>.>v..v>....>.v.>..>.vv>.>...",
">...>..vv.v..v..v..v..v..vv.>v.v...v..v.v>..v.>.>.>vv>>..vv..v>>>>>..>.v>.vvv.v...>..>>.>v>>v..>..v>.v>.v>.....>v..>>>vv..>.v>.>.......>...",
".v>...>>>.v.v..>>v..vv.v.v.v......>>>v.>v.v>..v..v>..>v.vv..>.....v....>>v>>....>...>>v..v...>v....v...v>v..v.>.>.vv.v>>vv....>.vv.v....>.v",
".>>.>>v...v.>v>vvv..v...>vv>>>v>v...>.>..>vv..>>>.v>..v>...>vvv.v>v..>.v>v>..>.>...>v....>.v.>....>...v..v.>.v>v...>..v..>v.v.>>>v.>..>v>>.",
">...>.>.vvv>>>v.>v.>>.v..vv.v.>>.>v.v..v...>..>>...v..vvv>.v>.....>>>...vv>vvv...>...v.......v>...>..v.>..>>..v>v....v..>v..v...v.v>...>...",
">..v.v.>vvvvv....v>>v>>v.>.....v....v...v>..v..v.>.>>....v>..v.v>>....>v......>..>>...>v>.vvv.v.>>>>v.v......v.>v>v......>.....vvv........v",
">>.v.>.v..>>.>.>v...v...>.>v>..v>.>v>>.......>....>>>...>v>>v..v...vvv.>...>......>>.vv>..>>>>>...>>v...v..>>.v.>...v...>..>..>..v.>......v",
".>.>>v.vv.>>v.....>vv...>>v>.>.v.>.vv.>...v....>...v.vv>.v..>...v>...>..>v...>>.>>....>.v.>.>..vv.>v>...vv...>>.....>vv.v.vv>vvv..>v..>.>..",
".v.v>.>...vvvv..>...v>v.>vv...v.v.v...vv.>...v..v>>>...vv.>>...>v...>.v>.v>v..vv>>....vv.>.vv..v.>.>..v.......v.v>v>>.v>>vv>v.>.>...>v.v>v.",
">.>v>vv>.>>>....>vv.v..vv>v>v..>..vvvv..vv..>vv.>.v...>.........>vvvvv...>>.v>v>..>v..v>.v.>.>.v..v......>vvvv...v>.>.vv..>>.vv.>>...v.>>..",
"..v...vv.vvv.>..v....v...v.vv>....vv..v..v..v.vv.v..vv..>>>...v.vv>...>..>v......v.v.vv>>v.v.v>.>v>.v.>.vv.v>v..>....v......vv>>v>>>..>....",
"..>..vv...>.>vv.>>..>...>v>..v>vv>.>.v>....>.v...>>v...>v....v.>v...>.>>.>.>v..v.vvv...v>>..v.vvv.>>v>v>v.v>..v>v..>>v....>.vv....v.v.>.v.v",
"v>..v...>..>v...v.v>.v>>vv>..>..v..>..v>>.......v..>...v..>.v..>..v...vv..vv>vv.v..>v...v>v>...>v>vv.v..>.>...v....v..>....v.v...>.......v.",
"v>.>v.>...v>.v>>..v>...v>.vvv.>v.>vv..vv.>.>..>.>>....>..v..v>.v>v.>.v>v.......v>>>vv..>v>>..v>.>..>v.>>v...v>...>.v..v>v....v.vv.>..v>vv..",
"..v...v......>v>.v...v>...>v...>.vv>v...>...>vv..vv.....>..vv....>v.>..v..>....>>v>.vv..>v>v.>>.>v.....>>...v...vv.v..>.>v>.>v>>v.vv>v>.>v.",
".>.v.vv..v>>.v..>.v>.>..>v>v....>..>v.v.>..>v.v>>v..>...v...>v.v>v...>v>.>v>.....v..v.v>.v.v.v..v...v..v.>.>vv>.v..v>v.v..vv>.>>vv.v...>...",
"..>.v.>..>vv.v....>.>.v.>>..>v.>..>>.>.......>.v.v>>.>......>>...v......v...v.vv.v>..v.>>v>>v>v>v.....>vvv.>>.>.>v..v>>.>...>.v...vv..>>v..",
">.>vvvv>.v..v>..v..vv....v.>v.>vv.v....v.>v.>v..>.vvv..v>.vv>..v..vvv.v..v..>..>..v...>>..>..>..v>vv.v>>vv>.v.vv.>..>..>v.v.>.v.....v.>>.v>",
">vv.v.>..>.>.>v>>>>.>.v.v......v>>>..>.....>v...v>.>>>.>>>.vv..v.........>........v....v.>>....>>vvv.>>..>..v>..v...vv.>>..>.>...>>>>..>...",
"vv..v...>.....v.....v.v.v..>>>.>>..>v>.>>..>v..>..>vv.v...v..>.>.......v>>>vv.>.v.>....>..>vvvvv..v..v>>v..v>.>>>.v..v...v>....>v...v.v..>>",
".v.>>...>.>..v.v...>v.v.>...>>vv.vv.v.>>.v...v..v..>.>...>>.....v>>.v>v.v>>..>....v.v.>.vv.>>v.>>v..v>..>.v>>.>v...v.>>v.>..>..v..v>>v.v>vv",
"v.>v...v.>.v...>vvv.>>...v..v>.vv>v.v.>.>v..v>v..>.v.>.>.vv>...>......>.>>v>>v.vv...>....>.>>...v>>.v..v>.>......v.v.v>..>.....v.>>v>v.>.>v",
".v>>v.>..>..v>...v>...vvv.v....v.v.>>.v.>..>v.v.>.v>>v>..>.v>..>v...vv..>.v>>>>vv..v..>.>.vv>vv>.v.>.>...v..>v...v...v.v..vvvv.>>>.v>.>v.>v",
"vv>..vv>>>v>.>..v..vvvv.v>.v.>v.>v.....>v>vv.>.>>>.v.>v..>...>>..v..>>........>.vvvv...vv>..v>v..vv>...>v>v>.v....>.>.>v>...vv..v>>.v>>.v.>",
"v..>.>........>>.>>>..>..>....vvvv.....>..>vv.v.>...>..v...>>v>v.v.v>>v.>>vvv>...v.>.>.>........vvv>v.>v>>>..>.v>.....v.>vv.v.>v..>.......>",
"..>vv.v..v..v>>v...v..>>>v>.v>>>vv.>..>v.>>.>..>.vv>>>>>..>..>.vvv.v.>.>>>>v>...>.>...v..v..v.v>.>..>>v.v>...v>.v.>v..>v.>...>.>v..>.....v."]


#Part 1, function to move cucumbers
def move(oldcucumbers):
    cucumbers = list(list(oldcucumbers))
    hswaps = []
    vswaps = []
    for i in range(len(cucumbers)):
        for j in range(len(cucumbers[0])):
            if cucumbers[i][j] == '>':
                if cucumbers[i][(j+1)%len(cucumbers[0])] == '.':
                    hswaps.append([[i,j],[i,(j+1)%len(cucumbers[0])]])
    for swap in hswaps:
        cucumbers[swap[0][0]][swap[0][1]], cucumbers[swap[1][0]][swap[1][1]] = cucumbers[swap[1][0]][swap[1][1]], cucumbers[swap[0][0]][swap[0][1]]
    for i in range(len(cucumbers)):
        for j in range(len(cucumbers[0])):
            if cucumbers[i][j] == 'v':
                if cucumbers[(i+1)%len(cucumbers)][j] == '.':
                    vswaps.append([[i,j],[(i+1)%len(cucumbers),j]])
    for swap in vswaps:
        cucumbers[swap[0][0]][swap[0][1]], cucumbers[swap[1][0]][swap[1][1]] = cucumbers[swap[1][0]][swap[1][1]], cucumbers[swap[0][0]][swap[0][1]]
    return cucumbers
#Function to turn cucumbers into one long string to check for equality
def totfunc(cucumbers):
    tot = ''
    for cucumber in cucumbers:
        for i in cucumber:
            tot += i
    return tot


#While loop to check if cucumbers moved after each turn
cucumbers = [[i for i in cucumber] for cucumber in puzzleinput]
count = 0
old = list(cucumbers)
while True:
    g1 = totfunc(old)
    g2 = totfunc(move(old))
    count += 1
    if g1 == g2:
        break
print(count)
#Part 2, solve every other puzzle which I've done
#I DID IT! I'M FREE!