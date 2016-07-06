#!/usr/bin/python

import copy

print
xmax = input("How many columns? ")
ymax = input("How many rows?    ")
pieces = input("How many parts?   ")

array = [[" " for y in range(ymax)] for x in range(xmax)]
piece = [[] for x in range(pieces)]

print
print "Let's design the parts. Use Spaces and any character, empty line to jump to the next:"

for count in range(pieces):
    print
    for y in range(ymax):
        line = raw_input("part "+str(count + 1)+" line "+str(y + 1)+": ")
        if line == "":
            break
        x = 0
        for letter in line:
            if letter != " ":
                piece[count] = piece[count] + [(x, y)]
            x += 1


def printarray(myarray):
    # print out the array when done. Digits 0-9 to indicate the parts, framed by *
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
    return


def checkpiece(mypiece):
    # check how many steps we can move the pieces to the right and down
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
        # if recursion level equals amount of parts and the last part matches we're done
            print "Resolved!"
            print
            printarray(mymatrix)
            exit(0)
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
                # everything matches, go to the next recursion
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
    # didn't match, return to the previous recursion
    return(mymatrix, level - 1, status)

print
print "Working ..."

array, level, status = main_loop(array, 0, 'success')

if status == 'fail':
    print "No match! Something wrong with the data?"
    exit(1)
