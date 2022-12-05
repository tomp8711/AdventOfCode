#DAY 3 Rucksack Reorganization
import re


with open("input.txt") as file:
        data =re.split(',|\n|-', file.read())
        total = 0
        count = 0
        while (count < len(data)):
            if int(data[count]) <= int(data[count+2]) and int(data[count+1]) >= int(data[count+3]):
                total+=1
            elif int(data[count]) >= int(data[count+2]) and int(data[count+1]) <= int(data[count+3]):
                total+=1
            count+=4



       
        print("---Part One--- ")
        print(total)

       
        total = 0
        count = 0
        while (count < len(data)):
            left = set(range(int(data[count]),int(data[count+1])+1))
            right = set(range(int(data[count+2]),int(data[count+3])+1))
            if left.intersection(right):
                total+=1
            count+=4
        print("---Part Two--- ")
        print(total)