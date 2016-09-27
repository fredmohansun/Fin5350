# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:28:56 2016

@author: sunmohan
"""

def getnum(a):
    return int(input(a)) # I don't know how to avoid user entering non-number characters but I want to
    
L=[] # L is all feasible nugget numbers
C=[] # C is a list contain nugget numbers in a roll

choice = getnum("Please enter all availabe nugget size, enter 0 to finish\n")

while choice != 0:
    L.append(choice)
    choice = getnum("Please enter all availabe nugget size, enter 0 to finish\n")

# Get all feasible nugget sizes

L.sort() # Make sure the list is in ascending sort

test = L[0] 
while len(C) < L[0]: # loop until I have L[0] nugget number in a roll in C
    sign = False # sign = true if the tested number is a nugget number
    test +=1 
    if test in L:
        continue
    for i in range(len(L)//2): # Assumption: Every nugget number must be a sum of two nugget number
        if test - L[i] in L:
            sign = True
            break
    if sign:
        L.append(test)
        C.append(test)
    else:
        C.clear() # Clear C if this tested number is not a nugget number
    L.sort()
print("Largest Impossible: ",L[len(L)-1]-L[0])