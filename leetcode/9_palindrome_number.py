# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 01:26:15 2021

@author: yanga
"""

import math

# solution 1, slow
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            temp_len = math.floor(math.log10(x))
            digit_list = []
            
            while temp_len >= 0:
                digit_list.append(x//(10**temp_len))
                x = x%(10**temp_len)
                temp_len = temp_len - 1
                
            check = True
            while len(digit_list) >= 2:
                if digit_list[0] == digit_list[-1]:
                    del digit_list[0]
                    del digit_list[-1]
                else:
                    check = False
                    break
            
            return check
        
           
Solution.isPalindrome(1, 5)
        


# solution 2, still slow

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            temp_len = math.floor(math.log10(x))
            
            if temp_len == 0:
                return True
            else:
                check = True
                
                i = 0
                while i < math.floor((temp_len + 1)/2):
                    curr_tail = (x%10)
                    curr_head = (x//(10**(temp_len - 2*i)))
                    
                    if curr_head != curr_tail:
                        check = False
                        break  
                    
                    x = x - curr_head*(10**(temp_len - 2*i))
                    x = x//10 
                    
                    if x == 0:
                        break
                    
                    i = i+1  
            
                return check


Solution.isPalindrome(1, 2222222)





class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False        
        else:
            return x == int(str(x)[::-1])


x = 2222222
















