#DAY 4 Camp Cleanup
import re



with open("input.txt") as file:
    data =re.split('\n\n', file.read())
    count = 0
    for val in data[0]:
        if val.isnumeric():
            count += 1
    total = 0
    stack = [ [] for _ in range(count) ]
    val = re.split('\n',data[0])
    for item in val[:-1]:
        whitespaceCount = 0
        idx = 0      
        for letter in item:
            if letter == ' ':
                whitespaceCount += 1
            else:
                whitespaceCount = 0
            if whitespaceCount == 4:
                idx += 1
                whitespaceCount = 0
            if letter.isalpha():
                stack[idx].append(letter)
                idx += 1
    movements = []
    for data in data[1].splitlines():
        movements.append(data.replace("move","").replace("from","").replace("to ","").split())
    
    for movement in movements:
      
        amount = int(movement[0])
        fromIdx = int(movement[1]) - 1
        toIdx = int(movement[2]) - 1
        for i in range(amount):
            temp = stack[fromIdx].pop(0)
            stack[toIdx].insert(0,temp)

    

    print("---Part One--- ")
    print((list(zip(*stack))[0]))




with open("input.txt") as file:
    data =re.split('\n\n', file.read())
    count = 0
    for val in data[0]:
        if val.isnumeric():
            count += 1
    total = 0
    stack = [ [] for _ in range(count) ]
    val = re.split('\n',data[0])
    for item in val[:-1]:
        whitespaceCount = 0
        idx = 0      
        for letter in item:
            if letter == ' ':
                whitespaceCount += 1
            else:
                whitespaceCount = 0
            if whitespaceCount == 4:
                idx += 1
                whitespaceCount = 0
            if letter.isalpha():
                stack[idx].append(letter)
                idx += 1
    movements = []
    for data in data[1].splitlines():
        movements.append(data.replace("move","").replace("from","").replace("to ","").split())
    
    for movement in movements:
        amount = int(movement[0])
        fromIdx = int(movement[1]) - 1
        toIdx = int(movement[2]) - 1
        newIdx = 0
        for i in range(amount):
            temp = stack[fromIdx].pop(0)
            stack[toIdx].insert(newIdx,temp)
            newIdx += 1

    print("---Part Two--- ")
    out = list(zip(*stack))[0]
    print(out)
