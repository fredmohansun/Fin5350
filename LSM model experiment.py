# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:14:17 2016

@author: sunmohan
LSM model experiment
"""

import numpy as np

## Setting Parameters

K = 40
T = 1
S0 = 41
sigma = .3
r = .08
div = 0
N = 4
M = 100000

## Calculating Parameters
h = T/N
nuh = (r-div-0.5*sigma*sigma)*h
sigsh = np.sqrt(h) * sigma

## X is for log(S)
X0 = np.log(S0)
XM = np.zeros((M,N+1))
XM[:,0] = X0

## Calculate X for N steps for M simulation, and get S matrix by exp(X)
for i in range(1,N+1):
    eps = np.random.standard_normal(M)
    XM[:,i] = XM[:,i-1] + nuh + sigsh *eps
    
S = np.exp(XM)

## CF is the matrix of value of option at each step, column 0 is an index
## Last column, or value at expiry, is the payoff at expury
CF = np.zeros((M,N+2))
CF[:,N+1] = np.maximum(K-S[:,N],0)

for i in range(M):
    CF[i][0]=i


## Recursion part on calculating CF
for i in range(N-1,0,-1):    
## Stemp is the column drawn from S, indStemp is used to check if option is in the money
    Stemp = S[:,i]
    ind = Stemp < K    
## Numtemp contains the row index of each dataset
    Numtemp = CF[:,0]    
## CFtemp is the PV of continuation value at the time horizon t = i
    ncol = N-i
    CFtemp1 = np.zeros((M,ncol))
    for k in range(ncol):
        CFtemp1[:,k] = CF[:,i+2+k]
        
    CFtemp = np.zeros(M)
        
    for j in range(ncol):
        CFtemp += CFtemp1[:,j] * np.exp(-r*h*(j+1))
    
    size = len(Stemp[ind])
## Linear Regression
    X = np.ones((size,3))
    X[:,0] = Stemp[ind]
    X[:,1] = Stemp[ind] * Stemp[ind]
    Y = CFtemp[ind]
    
    beta1, beta2, beta0 = np.linalg.lstsq(X,Y)[0]
## Calculate predict PV of Contiunation value and get the payoff at t = i
    CVhat = beta0 + beta1 * X[:,0] + beta2 * X[:,1]    
    Payofftemp = np.maximum(K-X[:,0],0)
    Num = Numtemp[ind]    
## if the PV of continuation value is less than payoff at t = i, individual
## choose to exercise early and get the payoff
    for j in range(size):
        if CVhat[j] < Payofftemp[j]:
                CF[Num[j]][i+1] = Payofftemp[j]
                CF[Num[j]][i+2] = 0.0
                
## End of recursion
                
                
                
## the value of option for each simulation is the sum of all PV of continuation value
for i in range(2,N+2):
    CF[:,1] += CF[:,i] * np.exp(-r*h*(i-1))
    
Sum = np.sum(CF[:,1])
price = Sum/M

print(price)
