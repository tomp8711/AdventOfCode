#DAY 1 Calorie Counting

import functools

def readFile(fileName: str) -> list:
    listInput = []
    with open(fileName) as file:
        for line in file:
            listInput.append(line.strip())
    return listInput


def getMax(listInput: list) -> int:
    
    maxCalorie = 0
    calories = 0
    for val in listInput:
        if val == "":
            calories = 0
        else:
            calories += int(val)
            maxCalorie = max(maxCalorie, calories)
    return  maxCalorie

def getThreeMax(listInput: list) -> int:
    
    calories = 0
    caloriesList = []
    for val in listInput:
        if val == "":
            caloriesList.append(calories)
            calories = 0
        else:
            calories += int(val)
    caloriesList.append(calories)
    maxCalories = sorted(caloriesList, reverse=True)[:3]
    return  sum(maxCalories) 

#better solution 
def solveReduce():
    with open("input.txt") as file:
        data = file.read().strip().split("\n\n")
        sumsV = []
        for part in data:
           # print(part.split())
            val = int(functools.reduce(lambda a,b: int(a)+int(b),part.split()))
            sumsV.append(val)
        print(max(sumsV))
        print(sum(sorted(sumsV)[-3:]))

#practice inspired by someone elses solution        
def solveMap():
     with open("input.txt") as file:
        data = file.read().strip().split("\n\n")
        sumsV = []
        for part in data:
            val = map(int, part.split())
            sumsV.append(sum(val))
        print(max(sumsV))
        print(sum(sorted(sumsV)[-3:]))


if __name__ == "__main__":
     inputPath = "input.txt"
     listInput = readFile(inputPath)
     maxCalorie = getMax(listInput)
     print("---Part One--- ")
     print(maxCalorie)

     maxCalorie = getThreeMax(listInput)
     print("---Part Two---")
     print(maxCalorie)
