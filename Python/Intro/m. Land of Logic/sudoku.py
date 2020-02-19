def sudoku(grid):
    for value in grid:
        if len(set(value)) != 9:
            return False
    for k in range(9):
        if len(set([i[k] for i in grid])) != 9:
            return False
    for i in range(0, len(grid), 3):
        for j in range(0, len(grid), 3):
            if len(set(grid[k][w] for w in range(j,j+3) for k in range(i,i+3))) != 9:
                return False
    return True

grid = [[1,3,2,5,4,6,9,8,7],
        [4,6,5,8,7,9,3,2,1],
        [7,9,8,2,1,3,6,5,4],
        [9,2,1,4,3,5,8,7,6],
        [3,5,4,7,6,8,2,1,9],
        [6,8,7,1,9,2,5,4,3],
        [5,7,6,9,8,1,4,3,2],
        [2,4,3,6,5,7,1,9,8],
        [8,1,9,3,2,4,7,6,5]]

print(sudoku(grid))