#!/usr/bin/python

#testarrays

pieces = 3
xmax = 4
ymax = 4

array = [[" " for x in range(xmax)] for y in range(ymax)]
piece = [" " for x in range(pieces)]

array = [[' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ']]


piece[0] = [(0,0),(1,0),(2,0),(3,0),(0,1)]
piece[1] = [(1,0),(2,0),(3,0),(0,1),(1,1),(2,1)]
piece[2] = [(3,0),(0,1),(1,1),(2,1),(3,1)]


#piece[0] = [(0,0),(1,0),(0,1),(1,1),(0,2),(0,3)]
#piece[1] = [(0,0),(1,0),(0,1),(1,1)]
#piece[2] = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]

def printarray(myarray):
    for y in range(ymax):
        outline = ""
        for x in range(xmax):
            outline = outline + str(myarray[x][y])
        print(outline)
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
    print "DEBUG loop starts"
    print "DEBUG: mymatrix, level, status", mymatrix, level, status
    if level == pieces:
        if status == 'success':
            print "DEBUG: We're done, it's resolved!"
            printarray(mymatrix)
            exit(0)
        else:
            print "DEBUG: no final match!"
            exit(1)
    mypiece = piece[level]
    xrot, yrot = checkpiece(mypiece)
    print "DEBUG: piece verified: mypiece, level, xrot, yrot:", mypiece, level, xrot, yrot
    status = 'success'
    y = 0
    print "DEBUG: start y loop to", yrot
    while y <= yrot:
        print "DEBUG: y", y
        print "DEBUG: start x loop to", xrot
        x = 0
        while x <= xrot:
            print "DEBUG: x", x
            piecestatus = 'success'
            newmatrix = mymatrix
            print "DEBUG: checking mypiece:", mypiece
            for i in mypiece:
                xcheck = i[0] + x
                ycheck = i[1] + y
                print "DEBUG: analyzing pos x, y:", xcheck, ycheck
                if newmatrix[xcheck][ycheck] != " ":
                    print "DEBUG: fail, there's a conflict at", xcheck, ycheck, "'", newmatrix[xcheck][ycheck], "'"
                    piecestatus = 'fail'
                    break
                else:
                    print "DEBUG: block matches, write to matrix at", xcheck, ycheck
                    newmatrix[xcheck][ycheck] = level
            if piecestatus == 'success':
                print "DEBUG: write to newmatrix and call next level:", newmatrix
                mymatrix, level, status = main_loop(newmatrix, level + 1, status)
            if status == 'fail':
                # continue
                print "DEBUG: had to go back one level, revert changes..."
                newmatrix = mymatrix
                print "DEBUG: mymatrix", mymatrix
            x += 1
        y += 1
    if status == 'fail':
        print "DEBUG: no solution, this shouldn't happen..."
        return(mymatrix, level, status)
    else:
        mymatrix = newmatrix
        printarray(mymatrix)
        return mymatrix, level, status

array, level, status = main_loop(array, 0, 'success')

