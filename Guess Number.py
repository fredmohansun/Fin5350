# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:48:07 2016

@author: sunmohan
"""

Play = True
while Play:
    print("\nPlease think of a positive integer between 0 - 100\n")
    Correct = False
    Guess = [0,100]
    marker = 0
    left = 0
    right = 100
    while not Correct:
        print("My guess is: ", Guess[marker])
        choice = input("please enter 1 if my guess is higher, enter 2 if my guess is lower, enter 3 if I'm correct.\n")
        if choice == "1":
            if Guess[marker] == 0:
                print("You cannot choose a negative number\n")
            else:
                right = Guess[marker]
                NextGuess = int((left+right)//2)
                if NextGuess in Guess:
                    print("Hey! No solution, did you tell a lie?\n")
                    Correct = True
                else:
                    if marker == len(Guess)-1:
                        Guess.append(NextGuess)
                    marker += 1
        elif choice == "2":
            if Guess[marker] == 100:
                print("You cannot choose a number greater than 100\n")
            else:
                left = Guess[marker]
                NextGuess = int((left+right)//2)
                if NextGuess in Guess:
                    print("Hey! No solution, did you tell a lie?\n")
                    Correct = True
                else:
                    if marker == len(Guess)-1:
                        Guess.append(NextGuess)
                    marker += 1
        elif choice == "3":
            Correct = True
            print("Yeah!!")
        else:
            print("Incorrect input!")
    N = input("If you don't want to play again, enter 0. Or enter anything else to play again\n")
    if N == "0":
        Play = False