#!/usr/bin/python

import copy
import time

#testarrays

pieces = 9
xmax = 9
ymax = 4

array = [[" " for y in range(ymax)] for x in range(xmax)]
piece = [" " for x in range(pieces)]


#array = [[' ', ' ', ' ', ' '],
#         [' ', ' ', ' ', ' '],
#         [' ', ' ', ' ', ' '],
#         [' ', ' ', ' ', ' ']]


#array = [[' ', ' ', ' ', ' ',' '],
#         [' ', ' ', ' ', ' ',' '],
#         [' ', ' ', ' ', ' ',' '],
#         [' ', ' ', ' ', ' ',' '],
#         [' ', ' ', ' ', ' ',' ']]

# to try 4x4

#piece[0] = [(0,0),(1,0),(2,0),(3,0),(0,1)]
#piece[1] = [(1,0),(2,0),(3,0),(0,1),(1,1),(2,1)]
#piece[2] = [(3,0),(0,1),(1,1),(2,1),(3,1)]

#piece[0] = [(0,0),(1,0),(0,1),(1,1),(0,2),(0,3)]
#piece[1] = [(0,0),(1,0),(0,1),(1,1)]
#piece[2] = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]

# to try 5x5

piece[0] = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)]
piece[1] = [(0,0),(1,0),(2,0),(3,0),(1,1)]
piece[2] = [(0,0),(1,0),(2,0),(3,0)]
piece[3] = [(1,0),(1,1),(0,2),(1,2)]
piece[4] = [(0,0),(1,0),(1,1),(2,1)]
piece[5] = [(0,0),(1,0),(0,1),(1,1)]
piece[6] = [(1,0),(0,1),(1,1),(2,1)]
piece[7] = [(0,0),(1,0),(1,1)]
piece[8] = [(0,0),(0,1)]

def printarray(myarray):
    delimiter = ''
    for x in range(xmax+2):
        delimiter = delimiter + "*"
    print(delimiter)
    for y in range(ymax):
        outline = "*"
        for x in range(xmax):
            outline = outline + str(myarray[x][y])
        outline = outline + "*"
        print(outline)
    print(delimiter)
    #time.sleep(0.1)
    return


def checkpiece(mypiece):
    xrot = xmax
    yrot = ymax
    xsize = 0
    ysize = 0
    for i in mypiece:
        if i[0] >= xsize:
            xsize = i[0] + 1
        if i[1] >= ysize:
            ysize = i[1] + 1
    xrot = xmax - xsize
    yrot = ymax - ysize
    return xrot, yrot



def main_loop(mymatrix, level, status):
    newmatrix = copy.deepcopy(mymatrix)
    if level == pieces:
        if status == 'success':
            print "We're done, it's resolved!"
            printarray(mymatrix)
            exit(0)
        else:
            print "No final match! Something's wrong with the data."
            exit(1)
    mypiece = piece[level]
    xrot, yrot = checkpiece(mypiece)
    status = 'success'
    y = 0
    while y <= yrot:
        x = 0
        while x <= xrot:
            piecestatus = 'success'
            for i in mypiece:
                xcheck = i[0] + x
                ycheck = i[1] + y
                if newmatrix[xcheck][ycheck] != " ":
                    piecestatus = 'fail'
                    newmatrix = copy.deepcopy(mymatrix)
                    break
                else:
                    newmatrix[xcheck][ycheck] = str(level)
            if piecestatus == 'success':
                for i in mypiece:
                    xcheck = i[0] + x
                    ycheck = i[1] + y
                    newmatrix[xcheck][ycheck] = str(level)
                printarray(newmatrix)
                newmatrix, level, status = main_loop(newmatrix, level + 1, 'success')
                if status == 'fail':
                    newmatrix = copy.deepcopy(mymatrix)
            else:
                newmatrix = copy.deepcopy(mymatrix)
            if status == 'fail':
                newmatrix = copy.deepcopy(mymatrix)
            x += 1
        y += 1
    status = 'fail'
    return(mymatrix, level - 1, status)

array, level, status = main_loop(array, 0, 'success')

