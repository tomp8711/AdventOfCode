#DAY 3 Rucksack Reorganization



with open("input.txt") as file:
        data = file.read().split("\n")
        total = 0
        for part in data:
            
            firsthalf, secondhalf = part[:len(part)//2], part[len(part)//2:]
            firstset = set(firsthalf)
            secondset = set(secondhalf)
            sharedLetter = firstset.intersection(secondset)
            if (list(sharedLetter)[0] == list(sharedLetter)[0].upper()):
                total += ord(list(sharedLetter)[0]) - 38
            else:
                total += ord(list(sharedLetter)[0]) - 96


       
        print("---Part One--- ")
        print(total)

        total = 0
        count = 0
        
        while(count < len(data)):
            firstSet = set(data[count])
            secondSet = set(data[count+1])
            thirdSet = set(data[count+2])
            sharedLetter = firstSet.intersection(secondSet)
            sharedLetter = sharedLetter.intersection(thirdSet)
            if (list(sharedLetter)[0] == list(sharedLetter)[0].upper()):
                total += ord(list(sharedLetter)[0]) - 38
            else:
                total += ord(list(sharedLetter)[0]) - 96
            count += 3


        
        print("---Part Two--- ")
        print(total)