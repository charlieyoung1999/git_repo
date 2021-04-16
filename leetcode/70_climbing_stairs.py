# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:12:32 2021

@author: yanga
"""


class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a=1
            b=2
            i = 3
            
            while i <= n:
                temp = a+b
                a=b
                b=temp
                i += 1
            
            
            return b
        

Solution.climbStairs(1,24)














