#DAY 8 Treetop Tree House
import numpy as np

with open("input.txt") as file:
    data = file.readlines()
    row, col = len(data[0].strip()), len(data)
    matrix = np.zeros((row,col), dtype=int)
    rowIdx = 0
    for line in data:
        colIdx = 0
        for num in line.strip():
            matrix[rowIdx][colIdx] = num
            colIdx += 1
        rowIdx += 1
    
    total = 2 * row + 2 * col - 4
    visible = True
   
    for i in range(1,row-1):
        for j in range(1,col-1):
            right = all(matrix[i][j] > list(matrix[i][j+1:col]))
            left = all(matrix[i][j] > list(matrix[i][0:j]))
            top = all(matrix[i][j] > list(matrix[0:i,[j]]))
            bottom = all(matrix[i][j] > list(matrix[i+1:row,[j]]))
            if right or left or top or bottom:
                total += 1

    print("---Part One--- ")
    print(total)

    total = 0
    for i in range(1,row-1):
        for j in range(1,col-1):
            right = matrix[i][j] > list(matrix[i][j+1:col])
            rcount = 0
            for bool in right:
                if bool == False:
                    rcount += 1
                    break
                rcount +=1
                
                
            left = matrix[i][j] > list(matrix[i][0:j])
            lcount = 0
            for bool in left[::-1]:
                if bool == False:
                    lcount +=1
                    break
                lcount += 1
            
            top = matrix[i][j] > list(matrix[0:i,[j]])
            tcount = 0
            for bool in top[::-1]:
                if bool == False:
                    tcount+=1
                    break
                tcount += 1

            bottom = matrix[i][j] > list(matrix[i+1:row,[j]])
            bcount = 0
            for bool in bottom:
                if bool == False:
                    bcount +=1
                    break
                bcount += 1
           
            score = lcount * rcount * tcount * bcount 
            total = max(total,score)   
    print("---Part Two--- ")         
    print(total)