# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:28:56 2016

@author: sunmohan
"""

def getnum(a):
    x = 'x'
    while x == 'x':
        try:
            x = int(float(input(a)))
        except:
            print("Invalid Input! Try again\n")
            x = 'x' 
    return x
    
# Make Sure all inputs are valid

def getchoice():
    A = []
    choice = getnum("Please enter all availabe nugget size, enter 0 to finish\n")
    while choice != 0 or len(A) == 0:
        if choice > 0:
            if choice not in A:
                A.append(choice)
            else:
                print("Already there")
        elif choice == 0 and len(A) == 0:
            print("There is nothing available, try again!")
        else:
            print("Please enter a positive number!\n")
        choice = getnum("Please enter all availabe nugget size, enter 0 to finish\n")
    return A

# Get all feasible nugget sizes
    
def ifmultiple(L):
    for i in range(2,max(L)+1,1):
        for j in L:
            if j % i != 0:
                break
        if j == max(L) and j % i == 0:
            return True
    return False

# Test if it's all even number

def main():
    L=getchoice() # L is all feasible nugget numbers
    C=[] # C is a list contain nugget numbers in a roll

    L.sort() # Make sure the list is in ascending sort

    Inf = [len(L)<=1,ifmultiple(L)]
    
    if any(Inf):
        raise RuntimeError("Warning! There might not be a solution because:\n\t\t\t\t(1)Too few size available or\n\t\t\t\t(2)All size share at least a common divisor")

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
        
    print("Largest Impossible: ",C[0]-1)
    
if __name__ == "__main__":
    main()
