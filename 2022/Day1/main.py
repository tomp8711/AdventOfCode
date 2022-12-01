#DAY 1 Calorie Counting

def readFile(fileName: str) -> list:
    listInput = []
    with open("input.txt") as file:
        for line in file:
            listInput.append(line.rstrip())
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

if __name__ == "__main__":
     inputPath = "./Day1/input.txt"
     listInput = readFile(inputPath)
     maxCalorie = getMax(listInput)
     print("---Part One --- ")
     print(maxCalorie)

     inputPath = "./Day1/input.txt"
     listInput = readFile(inputPath)
     maxCalorie = getThreeMax(listInput)
     print("---Part Two---")
     print(maxCalorie)
     
     

