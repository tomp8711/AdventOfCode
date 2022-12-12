#DAY 12 Hill Climbing Algorithm

def bfsSol(visited, queue, graph, start, end, grid):
    visited.append(start)
    queue.append((start, 0))
    while queue:
        loc, total = queue.pop(0)
        for i in ([(1,0), (-1,0), (0,1), (0,-1)]):
            neighbor =(loc[0] + i[0], loc[1] + i[1])
            if neighbor[0] >= len(grid[0]) or neighbor[0] < 0 or neighbor[1] >= len(grid) or neighbor[1] < 0:
                continue
            else:
                if graph[loc] == ord("z") and neighbor == end:
                    return total + 1
                elif neighbor not in visited and (graph[neighbor] == graph[loc] + 1 or graph[neighbor] <= graph[loc]) :
                    visited.append(neighbor)
                    queue.append((neighbor, total + 1))
def bfsSol2(visited, queue, graph, start, grid):
    visited.append(start)
    queue.append((start, 0))
    while queue:
        loc, total = queue.pop(0)
        for i in ([(1,0), (-1,0), (0,1), (0,-1)]):
            neighbor =(loc[0] + i[0], loc[1] + i[1])
            if neighbor[0] >= len(grid[0]) or neighbor[0] < 0 or neighbor[1] >= len(grid) or neighbor[1] < 0:
                continue
            else:

                if graph[loc] == ord("b") and graph[neighbor] == ord("a"):
                    return total + 1
                    
                elif neighbor not in visited and graph[loc] - 1 <= graph[neighbor] :
                    visited.append(neighbor)
                    queue.append((neighbor, total + 1))





with open("input.txt") as file:
    grid = []
    for line in file:
       grid.append(line.rstrip())

dict = {}
for y, line in enumerate(grid):
    for x, val in enumerate(line):
        dict[(x,y)] = ord(val)
        if val == "S":
            dict[(x,y)] = ord("a")
            start = (x,y)
        elif val == "E":
            dict[(x,y)] = ord("z")
            end = (x,y)
visited, queue = [], []
print("---Part One--- ")
print(bfsSol(visited, queue, dict, start, end, grid))
print("---Part Two--- ")
with open("input.txt") as file:
    grid = []
    for line in file:
       grid.append(line.rstrip())

dict = {}
for y, line in enumerate(grid):
    for x, val in enumerate(line):
        dict[(x,y)] = ord(val)
        if val == "E":
            dict[(x,y)] = ord("z") + 1
            start = (x,y)
visited, queue = [], []
print(bfsSol2(visited, queue, dict, start, grid))

