

def isSafe(row,col,nbr,sudoku):

    for i in range(9):    #exploring entire row
        if sudoku[row][i] == nbr:
            return False

    for i in range(9):    #exploring entire col
        if sudoku[i][col] == nbr:
            return False

    subrow = (row//3)*3
    subcol = (col//3)*3
    for i in range(3):
        for j in range(3):   #exploring sub matrix 3*3
            if sudoku[subrow+i][subcol+j] == nbr:
                return False

    return True

def printSudokuHelper(row,col,n,sudoku):

    if row == n:      #reached last position
        for i in sudoku:
            print(i)
        print()
        return

    while col < n and sudoku[row][col] != 0:    #if elements are already present
        col += 1

    if col == n:                                #if col range exceeds jump to next row
        printSudokuHelper(row+1,0,n,sudoku)

    for nbr in range(1,10):                     #to place numbers
        if isSafe(row,col,nbr,sudoku):
            sudoku[row][col] = nbr
            printSudokuHelper(row,col+1,n,sudoku)
            sudoku[row][col] = 0
    return

def printSudoku():

    sudoku = [[int(ele) for ele in input().split()] for i in range(9)]
    printSudokuHelper(0,0,9,sudoku)

printSudoku()
