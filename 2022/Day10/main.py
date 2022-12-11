#DAY 10 Cathode-Ray Tube
import math

def checkCycle(cycle: int, signal: int, signalStrengths: list) -> list:
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        signalStrengths.append(cycle * signal)
    return signalStrengths
with open("input.txt") as file:
    data = file.readlines()
    cycle = 0
    signal = 1
    signalStrengths = []
    for line in data:
        line = line.split()
        if line[0] == "noop":
            cycle += 1
            signalStrengths = checkCycle(cycle,signal,signalStrengths)
        else:
            cycle += 1
            signalStrengths = checkCycle(cycle,signal,signalStrengths)
            cycle += 1
            signalStrengths = checkCycle(cycle,signal,signalStrengths)
            signal += int(line[1])




           # print(signal)
    print("---Part One--- ") 
    print(sum(signalStrengths))

    print("---Part Two--- ") 
    with open("input.txt") as file:
        data = file.readlines()
        cycle = 0
        signal = 1
        spritePosition = 0
        row = ""
        for line in data:
            
            line = line.split()
            if line[0] == "noop":
                if cycle % 40 == 0 and len(row) > 0:
                    print(row)
                    row = ""
                if cycle % 40 == signal or cycle % 40 == signal - 1 or cycle % 40 == signal + 1:
                    row = row + "#"
                else: 
                    row = row + "."
                cycle += 1
                if cycle % 40 == 0 and len(row) > 0:
                    print(row)
                    row = ""
            else:
                if cycle % 40 == signal or cycle % 40 == signal - 1 or cycle % 40 == signal + 1:
                    row = row + "#"
                else: 
                    row = row + "."
                cycle += 1
                if cycle % 40 == 0 and len(row) > 0:
                    print(row)
                    row = ""
                if cycle % 40 == signal or cycle % 40 == signal - 1 or cycle % 40 == signal + 1:
                    row = row + "#"
                else: 
                    row = row + "."
                cycle += 1
                if cycle % 40 == 0 and len(row) > 0:
                    print(row)
                    row = ""
                signal += int(line[1])
