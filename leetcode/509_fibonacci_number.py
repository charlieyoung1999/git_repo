# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:59:27 2021

@author: yanga
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a = 0
            b = 1
            i = 2
            while i < n:
                temp = a + b
                a = b
                b = temp
                i = i+1
            return a+b
    






