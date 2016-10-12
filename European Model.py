# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:41:10 2016

@author: sunmohan
"""

import numpy as np

def OptionPrice(i,u,d,pu,pd,t,N,h,r,sigma):
    if t == N:
        i.get_payout()
        return i.payout
    Uoption = option(i.S*u,i.K,i.t)
    Doption = option(i.S*d,i.K,i.t)
    return np.exp(-r*h)*(pu*OptionPrice(Uoption,u,d,pu,pd,t+1,N,h,r,sigma)
        +pd*OptionPrice(Doption,u,d,pu,pd,t+1,N,h,r,sigma))
    
    

class option(object):
    
    def __init__(self,S,K,type):
        self.S = S
        self.K = K
        self.t = type
        self.payout = 0
        self.type = 0
        
    def numtype(self):
        try:
            a = {'c':1, 'C':1, 'p':2, 'P':2}
            self.type = a[self.t]
        except:
            print("invalid type")
    
    def get_payout(self):
        if self.type != 1 or self.type != 2:
            self.numtype()
        if self.type == 1:
            self.payout = max(self.S-self.K,0)
        elif self.type == 2:
            self.payout = max(self.K-self.S,0)
        
        


def main():
    # S0,K,sigma,h=T/N,r
    S0 = 100
    K=100
    N=2
    T=1
    h=T/N
    sigma=.30
    r=.08
    u = np.exp(r*h+sigma*np.sqrt(h))
    d = np.exp(r*h-sigma*np.sqrt(h))
    pu = (np.exp(r*h)-d)/(u-d)
    pd = 1-pu
    print(u,' ',d,' ',pu,' ',pd)
    Firstoption = option(S0,K,'p')
    price = OptionPrice(Firstoption,u,d,pu,pd,0,N,h,r,sigma)
    print(price)
    
if __name__ == "__main__":
    main()