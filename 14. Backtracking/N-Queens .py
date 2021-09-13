
def isSafe(row,col,n,board):

    #to check upward
    i = row-1
    while i >= 0:
        if board[i][col] == 1:
            return False
        i-=1

    #to check left diagonal
    i = row-1
    j = col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i-=1
        j-=1

    #ro check right diagonal
    i = row-1
    j = col+1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i-=1
        j+=1

    return True

def printpathHelper(row,n,board):

    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=' ')
        print()
        return

    for col in range(n):  #to explore columns
        if isSafe(row,col,n,board):    #if row,col isn't safe go to next col
            board[row][col] = 1
            printpathHelper(row+1,n,board)
            board[row][col] = 0
    return

def printpath(n):

    board = [[0 for j in range(n)] for i in range(n)]
    printpathHelper(0,n,board)

n = int(input())
printpath(n)
