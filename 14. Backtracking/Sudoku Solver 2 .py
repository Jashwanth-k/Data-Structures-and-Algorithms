
def isSafe(row,col,nbr,n,sudoku):

    for i in range(n):      #check entire row
        if sudoku[row][i] == nbr:
            return False

    for i in range(n):      #check entire column
        if sudoku[i][col] == nbr:
            return False

    subrow = (row//3)*3
    subcol = (col//3)*3
    for i in range(3):      #to check the sub 3*3 sudoku
        for j in range(3):
            if sudoku[subrow+i][subcol+j] == nbr:
                return False

    return True

def printSudokuHelper(row,col,n,sudoku):

    if row >= n:
        return True

    while col < n and sudoku[row][col] != 0:
        col += 1

    if col >= n:
        if printSudokuHelper(row+1,0,n,sudoku):
            return True

    for nbr in range(1,10):
        if isSafe(row,col,nbr,n,sudoku):
            sudoku[row][col] = nbr
            if printSudokuHelper(row,col+1,n,sudoku):
                return True
            sudoku[row][col] = 0


def printSudoku():

    n = 9
    sudoku = [[int(ele) for ele in input().split()] for i in range(n)]
    return printSudokuHelper(0,0,n,sudoku)

print(printSudoku())
