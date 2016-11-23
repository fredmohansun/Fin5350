# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:34:15 2016

@author: sunmohan
"""

import numpy as np
import scipy as sp
import abc

class VanillaOption(Object):
    
    def __init__(self, strike, expiry, payoff):
        self.__strike = strike
        self.__expiry = expiry
        self.__payoff = payoff
        
        @property
        def strike(self):