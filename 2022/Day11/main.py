#DAY 11 Monkey in the Middle
#Super hard coded for specific input

monkey0 = [71, 86]
monkey1 = [66, 50, 90, 53, 88, 85]
monkey2 = [97, 54, 89, 62, 84, 80, 63]
monkey3 = [82, 97, 56, 92]
monkey4 = [50, 99, 67, 61, 86]
monkey5 = [61, 66, 72, 55, 64, 53, 72, 63]
monkey6 = [59, 79, 63]
monkey7 = [55]

monkeyVisited = [0,0,0,0,0,0,0,0]
for i in range(20):
    #monkey 0 
    for i in range(len(monkey0)):
        worryLevel = monkey0[i] * 13
        worryLevel = worryLevel // 3
        if worryLevel % 19 == 0:
            monkey6.append(worryLevel)
        else:
            monkey7.append(worryLevel)
        monkeyVisited[0] += 1
    monkey0 = []

    #monkey1
    for i in range(len(monkey1)):
        worryLevel = monkey1[i] + 3
        worryLevel = worryLevel // 3
        if worryLevel % 2 == 0:
            monkey5.append(worryLevel)
        else:
            monkey4.append(worryLevel)
        monkeyVisited[1] += 1
    monkey1 = []

    #monkey2
    for i in range(len(monkey2)):
        worryLevel = monkey2[i] + 6
        worryLevel = worryLevel // 3
        if worryLevel % 13 == 0:
            monkey4.append(worryLevel)
        else:
            monkey1.append(worryLevel)
        monkeyVisited[2] += 1
    monkey2 = []

    #monkey3
    for i in range(len(monkey3)):
        worryLevel = monkey3[i] + 2
        worryLevel = worryLevel // 3
        if worryLevel % 5 == 0:
            monkey6.append(worryLevel)
        else:
            monkey0.append(worryLevel)
        monkeyVisited[3] += 1
    monkey3 = []

     #monkey4
    for i in range(len(monkey4)):
        worryLevel = monkey4[i] * monkey4[i]
        worryLevel = worryLevel // 3
        if worryLevel % 7 == 0:
            monkey5.append(worryLevel)
        else:
            monkey3.append(worryLevel)
        monkeyVisited[4] += 1
    monkey4 = []

     #monkey5
    for i in range(len(monkey5)):
        worryLevel = monkey5[i] + 4
        worryLevel = worryLevel // 3
        if worryLevel % 11 == 0:
            monkey3.append(worryLevel)
        else:
            monkey0.append(worryLevel)
        monkeyVisited[5] += 1
    monkey5= []

    #monkey6
    for i in range(len(monkey6)):
        worryLevel = monkey6[i] * 7
        worryLevel = worryLevel // 3
        if worryLevel % 17 == 0:
            monkey2.append(worryLevel)
        else:
            monkey7.append(worryLevel)
        monkeyVisited[6] += 1
    monkey6= []

    #monkey7
    for i in range(len(monkey7)):
        worryLevel = monkey7[i] + 7
        worryLevel = worryLevel // 3
        if worryLevel % 3 == 0:
            monkey2.append(worryLevel)
        else:
            monkey1.append(worryLevel)
        monkeyVisited[7] += 1
    monkey7= []

print("---Part One--- ") 
print(sorted(monkeyVisited,reverse=True)[0] * sorted(monkeyVisited,reverse=True)[1])

monkey0 = [71, 86]
monkey1 = [66, 50, 90, 53, 88, 85]
monkey2 = [97, 54, 89, 62, 84, 80, 63]
monkey3 = [82, 97, 56, 92]
monkey4 = [50, 99, 67, 61, 86]
monkey5 = [61, 66, 72, 55, 64, 53, 72, 63]
monkey6 = [59, 79, 63]
monkey7 = [55]

monkeyVisited = [0,0,0,0,0,0,0,0]
modVal = 19 * 2 * 13 * 5 * 7 * 11 * 17 * 3
for i in range(10000):
    #monkey 0 
    for i in range(len(monkey0)):
        worryLevel = monkey0[i] * 13
        worryLevel %= modVal
        if worryLevel % 19 == 0:
            # worryLevel = worryLevel / 19
            monkey6.append(worryLevel)
        else:
            monkey7.append(worryLevel)
        monkeyVisited[0] += 1
    monkey0 = []

    #monkey1
    for i in range(len(monkey1)):
        worryLevel = monkey1[i] + 3
        worryLevel %= modVal

        if worryLevel % 2 == 0:
            # worryLevel = worryLevel / 2
            monkey5.append(worryLevel)
        else:
            monkey4.append(worryLevel)
        monkeyVisited[1] += 1
    monkey1 = []

    #monkey2
    for i in range(len(monkey2)):
        worryLevel = monkey2[i] + 6
        worryLevel %= modVal

        if worryLevel % 13 == 0:
            # worryLevel = worryLevel / 13
            monkey4.append(worryLevel)
        else:
            monkey1.append(worryLevel)
        monkeyVisited[2] += 1
    monkey2 = []

    #monkey3
    for i in range(len(monkey3)):
        worryLevel = monkey3[i] + 2
        worryLevel %= modVal

        if worryLevel % 5 == 0:
            # worryLevel = worryLevel / 5
            monkey6.append(worryLevel)
        else:
            monkey0.append(worryLevel)
        monkeyVisited[3] += 1
    monkey3 = []

     #monkey4
    for i in range(len(monkey4)):
        worryLevel = monkey4[i] * monkey4[i]
        worryLevel %= modVal
        if worryLevel % 7 == 0:
            # worryLevel = worryLevel / 7
            monkey5.append(worryLevel)
        else:
            monkey3.append(worryLevel)
        monkeyVisited[4] += 1
    monkey4 = []

     #monkey5
    for i in range(len(monkey5)):
        worryLevel = monkey5[i] + 4
        worryLevel %= modVal
        if worryLevel % 11 == 0:
            # worryLevel = worryLevel/11
            monkey3.append(worryLevel)
        else:
            monkey0.append(worryLevel)
        monkeyVisited[5] += 1
    monkey5= []

    #monkey6
    for i in range(len(monkey6)):
        worryLevel = monkey6[i] * 7
        worryLevel %= modVal
        if worryLevel % 17 == 0:
            # worryLevel = worryLevel / 17
            monkey2.append(worryLevel)
        else:
            monkey7.append(worryLevel)
        monkeyVisited[6] += 1
    monkey6= []

    #monkey7
    for i in range(len(monkey7)):
        worryLevel = monkey7[i] + 7
        worryLevel %= modVal
        if worryLevel % 3 == 0:
            # worryLevel = worryLevel / 3
            monkey2.append(worryLevel)
        else:
            monkey1.append(worryLevel)
        monkeyVisited[7] += 1
    monkey7= []


print("---Part Two--- ") 
print(sorted(monkeyVisited,reverse=True)[0] * sorted(monkeyVisited,reverse=True)[1])
