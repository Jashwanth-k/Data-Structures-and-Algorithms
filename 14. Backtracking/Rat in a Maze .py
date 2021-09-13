
def printpathHelper(x,y,n,maze,solution):

    if x == n-1 and y == n-1:   #reached end in this case
        solution[x][y] = 1
        print(solution)

    #edge cases to stop exploring
    if x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0 or solution[x][y] == 1:
        return

    solution[x][y] = 1
    printpathHelper(x+1,y,n,maze,solution)    #exploring down
    printpathHelper(x-1,y,n,maze,solution)    #exploring up
    printpathHelper(x,y+1,n,maze,solution)    #exploring right
    printpathHelper(x,y-1,n,maze,solution)    #exploring left
    solution[x][y] = 0


def printpath(maze):

    n = len(maze)
    solution = [[0 for j in range(n)] for i in range(n)]
    printpathHelper(0,0,n,maze,solution)

n = int(input())
maze = [[int(ele) for ele in input().split()] for i in range(n)]
printpath(maze)

