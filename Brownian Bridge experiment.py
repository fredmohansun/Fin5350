# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 18:33:30 2016

@author: sunmohan
"""


import numpy as np
from scipy.stats import norm
from math import log2, sqrt

def CallPayoff(spot, strike):
    return np.maximum(spot - strike, 0.0)

def WienerBridge(expiry, num_steps, endval = 0.0):
    num_bisect = int(log2(num_steps))
    tjump = expiry
    ijump = int(num_steps - 1)
    
    if endval == 0.0: 
        endval = np.random.normal(scale=sqrt(expiry), size=1)

    z = np.random.normal(size=num_steps+1)
    w = np.zeros(num_steps+1)
    w[num_steps] = endval

    for k in range(num_bisect):
        left = 0
        i = ijump // 2 + 1
        right = ijump + 1
        limit = 2 ** k
        print(ijump,limit)

        for j in range(limit):
            print(k, j, i, left, right)
            a = 0.5 * (w[left] + w[right])
            b = 0.5 * sqrt(tjump)
            w[i] = a + b * z[i]
            
##Where I made a change, start here
            if j != limit - 1:
                right += ijump + 1
                left += ijump + 1
                i += ijump + 1
##Change End here

        ijump //= 2
        tjump /= 2

    return w


def StratifiedUniformSample(m = 100):
    u = np.random.uniform(size=m)
    i = np.arange(m)
    uhat = (i + u) / m
    return uhat

def GeometricBrownianMotionBridge(spot, mu, sigma, expiry, num_steps, num_reps):
    dt = expiry / num_steps
    nudt = (mu - 0.5 * sigma * sigma)*dt
    spaths = np.zeros((num_reps, num_steps+1))
    uhat = StratifiedUniformSample(num_reps)
    endval = norm.ppf(uhat)

    for i in range(num_reps):
        w = WienerBridge(expiry, num_steps)
        z = nudt + sigma * np.diff(w)
        lpath = np.cumsum(np.insert(z, 0, np.log(spot)))
        spaths[i] = np.exp(lpath)
        
    return spaths
    

def StratifiedMonteCarloPricer(spot, strike, rate, vol, expiry, div, num_steps, num_reps):
    spotT = GeometricBrownianMotionBridge(spot, rate, vol, expiry, num_steps, num_reps)
    callT = CallPayoff(spotT.T[-1], strike)
    callPrc = callT.mean() * np.exp(-rate * expiry)

    return callPrc

def main():
    spot = 41.0
    strike = 40.0
    rate = 0.08
    vol = 0.30
    div = 0.0
    expiry = 1.0
    num_steps = 10
    num_reps = 10000
    
    callPrc = StratifiedMonteCarloPricer(spot, strike, rate, vol, expiry, div, num_steps, num_reps)
    fmt = "The Call price via Stratified Monte Carlo is: {0:0.3f}".format(callPrc)
    print(fmt)

if __name__ == "__main__":
    main()