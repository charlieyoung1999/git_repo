# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 00:09:56 2021

@author: yanga
"""

class Solution:
    def reverse(self, x):
        if x > 0:
            temp = int(str(x)[::-1])
        else:
            temp = -int(str(-x)[::-1])
        
        if temp <= 2**31-1 and temp >= -2**31:
            return temp
        else:
            return 0
        

        
Solution.reverse(1, -1230)
        
x = 1534236469
        