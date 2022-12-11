#DAY 9 Rope Bridge
import math

def move(dir: str, head: list, tail: list) -> list:
    if dir == "R":
        head[0] += 1
        if math.dist(head,tail) == 2:
            tail[0] += 1
    if dir == "L":
        head[0] -= 1
        if math.dist(head,tail) == 2:
            tail[0] -= 1
    if dir == "U":
        head[1] += 1
        if math.dist(head,tail) == 2:
            tail[1] += 1
    if dir == "D":
        head[1] -= 1
        if math.dist(head,tail) == 2:
            tail[1] -= 1
    if math.dist(head,tail) > 2:
        if head[0] > tail[0] and head[1] > tail[1]:
            tail[0] += 1
            tail[1] += 1
        elif head[0] > tail[0] and head[1] < tail[1]:
            tail[0] += 1
            tail[1] -= 1
        elif head[0] < tail[0] and head[1] < tail[1]:
            tail[0] -= 1
            tail[1] -= 1
        else:
            tail[0] -= 1
            tail[1] += 1
    return head

def moveE(dir: str, head: list, tail: list) -> list:
    if math.dist(head,tail) == 2:
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
        elif head[1] < tail[1]:
            tail[1] -= 1
        elif head[1] > tail[1]:
            tail[0] += 1

    if math.dist(head,tail) > 2:
        if head[0] > tail[0] and head[1] > tail[1]:
            tail[0] += 1
            tail[1] += 1
        elif head[0] > tail[0] and head[1] < tail[1]:
            tail[0] += 1
            tail[1] -= 1
        elif head[0] < tail[0] and head[1] < tail[1]:
            tail[0] -= 1
            tail[1] -= 1
        else:
            tail[0] -= 1
            tail[1] += 1
    return  tail


with open("input.txt") as file:
    data = file.readlines()

    visited = set()
    head = [0,0]
    tail = [0,0]
    visited.add(str(tail[0])+"y"+str(tail[1]))
    for line in data:
        dir, dis = line.split()
        for i in range(int(dis)):
            move(dir,head,tail)
            visited.add(str(tail[0])+"y"+str(tail[1]))

    print("---Part One--- ") 
    print(len(visited))

with open("input.txt") as file:
    data = file.readlines()

    visited = set()
    head = [0,0]
    tail = [0,0]
    one = [0,0]
    two = [0,0]
    three = [0,0]
    four = [0,0]
    five = [0,0]
    six = [0,0]
    seven = [0,0]
    eight = [0,0]

    visited.add(str(tail[0])+"y"+str(tail[1]))
    for line in data:
        dir, dis = line.split()
        for i in range(int(dis)):
            
            head = move(dir,head,one)
            one = moveE(dir,head,one)
            two = moveE(dir,one,two)
            three = moveE(dir,two,three)
            four = moveE(dir,three,four)
            five = moveE(dir,four,five)
            six = moveE(dir,five,six)
            seven = moveE(dir,six,seven)
            eight = moveE(dir,seven,eight)
            tail = moveE(dir,eight,tail)
            visited.add(str(tail[0])+"y"+str(tail[1]))
    print("---Part Two--- ") 
    print(len(visited))




