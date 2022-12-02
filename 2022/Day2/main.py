#DAY 2 Rock Paper Scissors

RpsDict = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

RpsDict2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


with open("input.txt") as file:
        data = file.read().split("\n")
        total = 0
        for part in data:
            total += RpsDict[part]
       
        print("---Part One--- ")
        print(total)

        total = 0
        for part in data:
            total += RpsDict2[part]
        print("---Part Two--- ")
        print(total)