# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:36:39 2021

@author: yanga
"""

class Solution:
    def mySqrt(self, x):
        import math        
        return math.floor(math.sqrt(x))
        



class Solution:
    def mySqrt(self, x):
        
        i = 1
        
        while i < x:
            if i*i <= x and (i+1)*(i+1) > x:
                return i
        

x = 8





