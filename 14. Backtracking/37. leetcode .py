
def isSafe(row ,col ,nbr ,n ,sudoku):

    for i in range(n):  # check entire row
        if sudoku[row][i] == nbr:
            return False

    for i in range(n):  # check entire column
        if sudoku[i][col] == nbr:
            return False

    mainrow = (row//3 ) *3
    maincol = (col//3 ) *3
    for i in range(3):  # to check the sub 3*3 sudoku
        for j in range(3):
            if sudoku[mainrow +i][maincol +j] == nbr:
                return False

    return True

def printSudokuHelper(row ,col ,n ,sudoku):

    if row >= n:
        print(sudoku)
        return

    while col < n and sudoku[row][col] != '.':
        col += 1

    if col >= n:
        printSudokuHelper(row +1 ,0 ,n ,sudoku)

    for nbr in range(1,10):
        if isSafe(row ,col ,str(nbr) ,n ,sudoku):
            sudoku[row][col] = str(nbr)
            printSudokuHelper(row ,col +1 ,n ,sudoku)
            sudoku[row][col] = '.'


def printSudoku(board):

    n = 9
    printSudokuHelper(0 ,0 ,n ,board)

class Solution:
    def solveSudoku(self, board):
        printSudoku(board)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

Solution.solveSudoku(Solution,board)
