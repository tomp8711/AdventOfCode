#DAY 7 No Space Left On Device

with open("input.txt") as file:
    data = file.read().split("\n")
    totals = {}
    nestedLetter = {}
    order = []
    currentKey = ""
    i = 0
    while(i < len(data)):
        if "cd " in data[i] and "cd .." not in data[i]:
            currentKey = currentKey +  data[i].split()[2]
            order.append(currentKey)
            totals.update({currentKey:0})
            nestedLetter.update({currentKey: list()})
            i = i+1
        elif "ls" in data[i] and "$" in data[i]:
            continue        
        elif "dir " in data[i]:
            nestedLetter[currentKey].append(currentKey + data[i].split()[1])
        elif "cd .." in data[i] and "$" in data[i]:
            order.pop()
            currentKey = order[-1]
           
        else:
            totals[currentKey] += int(data[i].split()[0])

        i = i+1   
    

    keys = list(nestedLetter.keys())
    keys.reverse()
    
    total = 0
    for key in keys:
        val = 0
        if (len(nestedLetter[key]) > 0):
            for idx in nestedLetter[key]:
                val += totals[idx]
        totals[key] += val
        if (totals[key] <= 100000):
            total += totals[key]

    
    print("---Part One--- ")
    print(total)


    total = 100**100
    expected = 30000000 - (70000000 - totals['/'])
    for totalValue in totals:
        if totals[totalValue] >= expected:
            total = min(total, totals[totalValue])

    print("---Part Two--- ")
    print(total)