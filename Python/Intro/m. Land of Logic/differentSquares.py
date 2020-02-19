# def differentSquares(matrix):
#     count = (len(matrix[0])-1)*(len(matrix)-1)
#     return count-2 if count else count
def differentSquares(matrix):
    s = set()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            s.add(str(matrix[i][j]) + ' ' + str(matrix[i][j+1]) + ' ' +str(matrix[i+1][j]) + ' ' + str(matrix[i+1][j+1]))
    return len(s)
