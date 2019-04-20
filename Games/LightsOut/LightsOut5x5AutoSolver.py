'''Note: this solving algorithm does not solve optimally'''

import numpy as np
import random

Board = np.zeros((5, 5), dtype=int)  # Make Blank 5x5 board
clicks = 0

    
def Click(x, y):
    # Change light of selected button
    if Board[y - 1, x - 1] == 0: Board[y - 1, x - 1] = 1
    else: Board[y - 1, x - 1] = 0

    # Change light to the left
    if x > 1:
        if Board[y - 1, x - 2] == 0: Board[y - 1, x - 2] = 1
        else: Board[y - 1, x - 2] = 0
        
    # Change light to the right
    if x < 5:
        if Board[y - 1, x] == 0:  Board[y - 1, x] = 1
        else: Board[y - 1, x] = 0
        
    # Change light above
    if y > 1:
        if Board[y - 2, x - 1] == 0: Board[y - 2, x - 1] = 1
        else: Board[y - 2, x - 1] = 0
        
    # Change light below
    if y < 5:
        if Board[y, x - 1] == 0: Board[y, x - 1] = 1
        else: Board[y, x - 1] = 0


def Manual():  # manually input points to be clicked
    x, y = input("(x,y): ").replace(",", " ").split()  # get particular light to click
    x, y = int(x), int(y)  # convert to int
    Click(x, y)  # click the light


def Manual2():  # manually input which lights are "on"
    x, y = input("(x,y): ").replace(",", " ").split()
    x, y = int(x), int(y)

    if Board[y - 1, x - 1] == 0: Board[y - 1, x - 1] = 1
    else: Board[y - 1, x - 1] = 0

    
def LightChase():
    clicks = 0
    
    # Chase lights down to bottom row
    for y in range(2, 6):
        for x in range(1, 6):
            if Board[y - 2, x - 1] == 1:
                Click(x, y)
                clicks += 1

    # Check bottom row state and click applicable top row lights
    if Board[4, 0] == 1 and Board[4, 1] == 0 and Board[4, 2] == 0 and Board[4, 3] == 0 and Board[4, 4] == 1:
        Click(1, 1)
        Click(2, 1)
        clicks += 2
        
    elif Board[4, 0] == 0 and Board[4, 1] == 1 and Board[4, 2] == 0 and Board[4, 3] == 1 and Board[4, 4] == 0:
        Click(1, 1)
        Click(4, 1)
        clicks += 2
        
    elif Board[4, 0] == 1 and Board[4, 1] == 1 and Board[4, 2] == 1 and Board[4, 3] == 0 and Board[4, 4] == 0:
        Click(2, 1)
        clicks += 1
        
    elif Board[4, 0] == 0 and Board[4, 1] == 0 and Board[4, 2] == 1 and Board[4, 3] == 1 and Board[4, 4] == 1:
        Click(4, 1)
        clicks += 1
        
    elif Board[4, 0] == 1 and Board[4, 1] == 0 and Board[4, 2] == 1 and Board[4, 3] == 1 and Board[4, 4] == 0:
        Click(5, 1)
        clicks += 1
        
    elif Board[4, 0] == 0 and Board[4, 1] == 1 and Board[4, 2] == 1 and Board[4, 3] == 0 and Board[4, 4] == 1:
        Click(1, 1)
        clicks += 1
        
    elif Board[4, 0] == 1 and Board[4, 1] == 1 and Board[4, 2] == 0 and Board[4, 3] == 1 and Board[4, 4] == 1:
        Click(3, 1)
        clicks += 1
        
    else: return clicks  # Board already solved

    # Chase lights down to solved state
    for y in range(2, 6):
        for x in range(1, 6):
            if Board[y - 2, x - 1] == 1:
                Click(x, y)
                clicks += 1
                
    return clicks

    
def main():
    level = int(input("Level: "))
    boards = int(input("Boards: "))

    while boards > 0:
        # Create a random board by clicking randomly [level] times
        for i in range(level): Click(random.randint(1, 5), random.randint(1, 5))

        # Solve the board (suboptimally) and print #of clicks to solve
        solveClicks = LightChase()
        print(solveClicks)
        
        boards -= 1


main()

'''
x is the horizonal and increases from left to right from 1 to 5 inclusive
y is the vertical and increases from top to bottom from 1 to 5 inclusive

For example, the top-leftmost box is (1,1); the middle is (3,3)

When using manual modes...
The program will return how many clicks it took using the "Light Chasing" method.
'''