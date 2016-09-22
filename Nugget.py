# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:28:56 2016

@author: sunmohan
"""

L=[6,9,12,15,18,20]
C=[]
sign = False
for i in range(21,65536):
    sign = False
    if i % 2 ==0:
        middlel=i/2
        middler=i/2
    else:
        middlel=i//2
        middler=i//2+1
    for j in range(11):
        if middlel-j in L and middler+j in L:         
            sign = True            
            break
    if sign:
        L.append(i)
        C.append(i)
        if len(C) >= 6:
            print("Largest Impossible: ",L[len(L)-1]-6)
            break
    else:
        C.clear()
    
