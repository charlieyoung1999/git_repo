# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        else:          
            temp = []
            for i in range(1,math.floor(math.sqrt(num))+1):
                if num%i == 0:
                    if i == 1:
                        temp.append(i)
                    elif i == math.sqrt(num):
                        temp.append(math.sqrt(num))
                    else:
                        temp.append(i)
                        temp.append(num/i)
            
            return(sum(temp) == num)
    

       