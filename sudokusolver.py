#
# Written entirely by @DuncanLamont
#


# Board[][] first list is of the rows, second is numbers in each row
board = [
    [0,0,4,9,7,0,2,3,5],
    [5,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,9,8],
    [0,6,0,0,2,5,0,0,0],
    [4,0,0,0,0,0,0,0,1],
    [0,0,0,6,4,0,0,5,0],
    [6,7,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,9],
    [1,9,2,0,5,4,8,0,0]
]
# Board of truths is basically helps me see which spots have been cleared,
# which spots are true and false. Hence board of truth
board_of_truths = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

# Prints board similar to the way a human would interpret it.
def printboard():
    print("Sudoku Board")
    for i in range(9):
        if (i == 3 or i == 6):
            print("")
        print("[ "+ str(board[i][0]) + " " + str(board[i][1]) + " " + str(board[i][2]) + " ] [ " + str(board[i][3]) + " " + str(board[i][4]) + " " + str(board[i][5]) + " ] [ " + str(board[i][6]) + " " + str(board[i][7]) + " " + str(board[i][8]) + " ]")
# Prints board of truth similar to a way a human would interpret it.
def printboardt():
    print("Board of Truth")
    for i in range(9):
        if (i == 3 or i == 6):
            print("")
        print("[ "+ str(board_of_truths[i][0]) + " " + str(board_of_truths[i][1]) + " " + str(board_of_truths[i][2]) + " ] [ " + str(board_of_truths[i][3]) + " " + str(board_of_truths[i][4]) + " " + str(board_of_truths[i][5]) + " ] [ " + str(board_of_truths[i][6]) + " " + str(board_of_truths[i][7]) + " " + str(board_of_truths[i][8]) + " ]")


def resettruth():
    global board_of_truths 
    board_of_truths = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
# The check function outputs whether or not this square can be number n.
# Check is a function that takes in the number we're interested in,
# the board, and the x,y position of the square in question. We return
# False if the square CAN'T be the number, ideally we want true.
def check(n,x,y) :
    startx = 0
    starty = 0
    if(board[y][x] != 0):
        return False
        
    for i in range(9):
        if(((board[i][x] == n) or (board[y][i]) == n)):
            return False
    if(x<3):
        startx = 0
    elif(x>5):
        startx = 6
    else:startx = 3

    if(y<3):
        starty = 0
    elif(y>5):
        starty = 6
    else:starty = 3

    for l in range(3):
                for k in range(3):
                    if(board[starty+l][startx+k] == n):
                        return False
    return True

# Find determines if number n is at coordinate x,y
def find(n,x,y):
    if(board[y][x] == n):
        return True
    else: return False




# Basically open spot solver uses each 3x3 square along with the rows
# to try and solve a spot in that 3x3. For example, if the entire square
# is empty, but the other 3x3 squares in the puzzle all have their 1's
# filled in, there is only one spot for the remaining 1, this func 
# should recognize that. This should actually get quite a few squares
# on basic puzzles.
def open_spot_solver(n):
    x = 0
    y = 0
    # iterating thru each 3x3, there are 9 of them
    for i in range(9):
        if(i < 3):
            x = i * 3
            y = 0
            for l in range(3):
                for k in range(3):
                    if(check(n,x+l,y+k)):
                        board_of_truths[y+k][x+l] = 1
                        
        if((i >= 3) and (i < 6)):
            x = (i-3) * 3
            y = 3
            for l in range(3):
                for k in range(3):
                    if(check(n,x+l,y+k)):
                        board_of_truths[y+k][x+l] = 1
        if(i>5):
            x = (i-6) * 3
            y = 6
            for l in range(3):
                for k in range(3):
                    if(check(n,x+l,y+k)):
                        board_of_truths[y+k][x+l] = 1

# Post board of truth attempts to fill in the numbers that open spot
# solver found.
def post_board_of_truth(n):
    counter = 0
    for i in range(9):
        if(i < 3):
            x = i * 3
            y = 0
            for l in range(3):
                for k in range(3):
                    if(board_of_truths[y+k][x+l] == 1):
                        counter += 1
            while(counter == 1):
                for l in range(3):
                    for k in range(3):
                        if(board_of_truths[y+k][x+l] == 1):
                            board[y+k][x+l] = n
                            counter = 0
        if((i >= 3) and (i < 6)):
            x = (i-3) * 3
            y = 3
            for l in range(3):
                for k in range(3):
                    if(board_of_truths[y+k][x+l] == 1):
                        counter += 1
            while(counter == 1):
                for l in range(3):
                    for k in range(3):
                        if(board_of_truths[y+k][x+l] == 1):
                            board[y+k][x+l] = n
                            counter = 0
        if(i>5):
            x = (i-6) * 3
            y = 6
            for l in range(3):
                for k in range(3):
                    if(board_of_truths[y+k][x+l] == 1):
                        counter += 1
            while(counter == 1):
                for l in range(3):
                    for k in range(3):
                        if(board_of_truths[y+k][x+l] == 1):
                            board[y+k][x+l] = n
                            counter = 0
                        

# Basically the solver recursively                            
def putting_her_together():
    # Flag indicates whether or not we've gotten any gold this time around.
    #flag = False
    printboard()


    for i in range(50):
        for j in range(9):
            open_spot_solver(j+1)
            post_board_of_truth(j+1)
            resettruth()
    print("Final product")
    printboard()
    



            
# Testing area:
putting_her_together()
