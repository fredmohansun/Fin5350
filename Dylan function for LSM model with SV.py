# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:14:17 2016

@author: sunmohan
LSM model experiment
"""



def LSMpricer(pricing_engine, option, data):
    T = option.expiry
    K = option.strike
    (S0, r, Vbar, div) = data.get_data()
    M = pricing_engine.reps
    N = pricing_engine.steps
    alpha = .5
    xi = 0.02
    h = T/N
    alphah = alpha * h
    xish = xi * np.sqrt(h)
    
    X0 = np.log(S0)
    XM = np.zeros((M,N+1))
    XM[:,0] = X0
    
    V = np.zeros((M,N+1))
    V[:,0] = Vbar
    
    for i in range(1,N+1):
        eps1 = np.random.standard_normal(M)
        V[:,i] = V[:,i-1] + alphah * (Vbar-V[:,i-1]) + xish * eps1
        nuh = (r-div-0.5*V[:,i-1]*V[:,i-1])*h
        sigsh = np.sqrt(h) * V[:,i-1]
        eps2 = np.random.standard_normal(M)
        XM[:,i] = XM[:,i-1] + nuh + sigsh *eps2
        
    S = np.exp(XM)

    CF = np.zeros((M,N+2))
    CF[:,N+1] = option.payoff(S[:,N])
    
    for i in range(M):
        CF[i][0]=i

    for i in range(N-1,0,-1):
        Stemp = S[:,i]
        ind = Stemp < K
        Numtemp = CF[:,0]
        ncol = N-i
        CFtemp1 = np.zeros((M,ncol))
        
        for k in range(ncol):
            CFtemp1[:,k] = CF[:,i+2+k]
            
        CFtemp = np.zeros(M)
        
        for j in range(ncol):
            CFtemp += CFtemp1[:,j] * np.exp(-r*h*(j+1))

        size = len(Stemp[ind])
        
        X = np.ones((size,3))
        X[:,0] = Stemp[ind]
        X[:,1] = Stemp[ind] * Stemp[ind]
        Y = CFtemp[ind]
        
        beta1, beta2, beta0 = np.linalg.lstsq(X,Y)[0]
        
        CVhat = beta0 + beta1 * X[:,0] + beta2 * X[:,1]    
        Payofftemp = option.payoff(X[:,0])
        Num = Numtemp[ind]   
        
        for j in range(size):
            if CVhat[j] < Payofftemp[j]:
                    CF[Num[j]][i+1] = Payofftemp[j]
                    CF[Num[j]][i+2] = 0.0
    
    for i in range(2,N+2):
        CF[:,1] += CF[:,i] * np.exp(-r*h*(i-1))

    Sum = np.sum(CF[:,1])
    price = Sum/M
    
    return price
