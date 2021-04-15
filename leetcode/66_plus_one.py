# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 01:34:41 2021

@author: yanga
"""

class Solution:
    def plusOne(self, digits):
        
        i = len(digits)-1
        
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1
            
        digits.insert(0,1)
        return(digits) 
                
        






        
        
        
digits = [9,9]


Solution.plusOne(1, [9,9])

     
# another solution: way faster
class Solution:
    def plusOne(self, digits):
        digits = map(str, digits)
        digits = "".join(digits)
        digits = int(digits)
        digits += 1        
        digits = str(digits)
        return [x for x in digits]
        




















