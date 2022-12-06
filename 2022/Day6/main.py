#DAY 4 Camp Cleanup
import re


with open("input.txt") as file:
    data = file.read()

    dataLength = len(data)

    for i in range(dataLength - 3):
        
        if len(set(data[i:i+4])) == 4:
            total = i + 4
            break
        
    
    print("---Part One--- ")
    print(total)

    for i in range(dataLength - 13):
            
            if len(set(data[i:i+14])) == 14:
                total = i + 14
                break
        
    print("---Part Two--- ")
    print(total)
