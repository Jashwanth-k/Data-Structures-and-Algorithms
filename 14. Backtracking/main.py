
def isSafe(row, col, nbr, n, sudoku):
    for i in range(n):  # check entire row
        if sudoku[row][i] == nbr:
            return False

    for i in range(n):  # check entire column
        if sudoku[i][col] == nbr:
            return False

    subrow = (row // 3) * 3
    subcol = (col // 3) * 3
    for i in range(3):  # to check the sub 3*3 sudoku
        for j in range(3):
            if sudoku[subrow + i][subcol + j] == nbr:
                return False

    return True


def printSudokuHelper(row, col, n, sudoku):
    if row >= n:
        return True

    while col < n and sudoku[row][col] != '.':
        col += 1

    if col >= n:
        if printSudokuHelper(row + 1, 0, n, sudoku):
            return True

    for nbr in range(1, 10):
        if isSafe(row, col, str(nbr), n, sudoku):
            sudoku[row][col] = str(nbr)
            if printSudokuHelper(row, col + 1, n, sudoku):
                return True
            sudoku[row][col] = '.'

def printSudoku(board):
    n = 9
    if printSudokuHelper(0, 0, n, board):
        return True
    else:
        return False

class Solution:
    def isValidSudoku(self, board):
        print(printSudoku(board))

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Solution.isValidSudoku(Solution,board)
