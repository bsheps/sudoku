gameBoard1 = [
    [0,7,0,0,2,3,0,9,6],
    [0,0,2,0,0,0,0,7,0],
    [9,0,0,0,5,6,0,0,3],
    [4,0,9,0,0,0,6,0,0],
    [0,3,0,5,4,1,0,2,0],
    [0,0,7,0,0,0,3,0,4],
    [8,0,0,1,9,0,0,0,5],
    [0,9,0,0,0,0,1,0,0],
    [2,1,0,4,3,0,0,6,0],
]
gameBoard2 = [
    [0,0,8,0,0,1,0,3,0],
    [7,0,1,0,0,0,8,9,0],
    [2,6,5,0,0,3,0,0,7],
    [0,1,4,0,7,0,0,0,8],
    [0,0,2,8,0,9,7,0,0],
    [8,0,0,0,4,0,6,5,0],
    [1,0,0,3,0,0,2,8,5],
    [0,2,6,0,0,0,3,0,4],
    [0,8,0,4,0,0,1,0,0]
]
line = " -----------------------"

def solve(gameBoard):
    cell = findEmptyCell(gameBoard)
    if cell is not None:
        r = cell[0]
        c = cell[1]
        for n in range(1,10):
            gameBoard[r][c] = n
            if isValidBoard(gameBoard):
                if isSolution(gameBoard):
                    printBoard(gameBoard)
                else:
                    solve(gameBoard)
            gameBoard[r][c] = 0

def findEmptyCell(gameBoard):
    col = 0
    row = 0
    while row < 9:
        while col < 9:
            if gameBoard[row][col] == 0: #empty cell
                return [row,col]
            col += 1
        col = 0 # new row, reset col
        row += 1

def isSolution(gameBoard):
    return isValidBoard(gameBoard) and isFilled(gameBoard)

def isValidBoard(gameBoard):
    for row in gameBoard:
        if(not validRow(row)):
            return False
    for col in range(0,len(gameBoard[0])):
        if not validCol(gameBoard, col):
            return False
    return allSquaresValid(gameBoard)

def validRow(row):
    values = []
    for cell in row:
        if cell > 0:
             values.append(cell)
    return len(values) == len(set(values))

def validCol(board, col):
    values=[]
    for row in board:
        if row[col] > 0:
            values.append(row[col])
    
    return len(values) == len(set(values))

def allSquaresValid(gameBoard):
    return (validSquare(gameBoard,0,2,0,2) and 
            validSquare(gameBoard,3,5,0,2) and 
            validSquare(gameBoard,6,8,0,2) and
            validSquare(gameBoard,0,2,3,5) and 
            validSquare(gameBoard,3,5,3,5) and 
            validSquare(gameBoard,6,8,3,5) and
            validSquare(gameBoard,0,2,6,8) and 
            validSquare(gameBoard,3,5,6,8) and 
            validSquare(gameBoard,6,8,6,8)
           )

def validSquare(board, x1, x2, y1, y2):
    values=[]
    for row in range(x1,x2+1):
        for col in range(y1, y2+1):
            if board[row][col] > 0:
                values.append(board[row][col])
    return len(values) == len(set(values))

def isFilled(gameBoard):
    for row in gameBoard:
        for cell in row:
            if cell == 0:
                return False
    return True

def printBoard(board):
    for row in range(len(board)):
        if row % 3 == 0:
            print(line)
        for col in range(len(board[row])):
            if col % 3 == 0:
                print("| ",end='')
            if board[row][col] == 0:
                print("  ", end='')
            else:
                print(board[row][col] ,end=' ')
        print('|')
    print(line, '\n')

printBoard(gameBoard1)
print(solve(gameBoard1))
printBoard(gameBoard2)
print(solve(gameBoard2))
