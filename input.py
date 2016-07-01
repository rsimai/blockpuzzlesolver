#!/usr/bin/python

print "Some basic information"

ymax = input("How many columns? ")
xmax = input("How many rows? ")
amountofpieces = input("How many pieces? ")

print "Let's design the pieces"

for count in range(amountofpieces):
    for y in range(ymax):
        line = input(count)



