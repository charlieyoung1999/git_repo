# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 01:38:44 2021

@author: yanga
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        else:
            temp = 0
            
            i = 0           
            check = True
            
            while i < min(list(map(len, strs))):
                j = 1                
                while j < len(strs):
                    if strs[j][i] != strs[0][i]:
                        check = False
                        break
                    else:
                        j = j+1                    
                
                if check:
                    temp = temp + 1
                    i = i+1
                else:
                    break
            
            if temp > 0:
                return strs[0][:temp]
            else:
                return ""
                
        
        
        
        
        
        
strs = ["dog","racecar","car"]     
strs = ["flower","flow","flight"]     
        
Solution.longestCommonPrefix(1, strs)
        




    