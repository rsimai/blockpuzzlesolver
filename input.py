#!/usr/bin/python

print "Some basic information"

ymax = input("How many columns? ")
xmax = input("How many rows? ")
pieces = input("How many pieces? ")

piece = [[] for x in range(pieces)]

print "Let's design the pieces"

for count in range(pieces):
    for y in range(ymax):
        line = raw_input(count)
        x = 0
        for letter in line:
            if letter != " ":
                piece[count] = piece[count] + [(x,y)]
            x += 1
        print piece[count]



