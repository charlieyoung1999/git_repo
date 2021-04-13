# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 00:21:22 2021

@author: yanga
"""

class Solution:
    def convert(self, s, numRows):
        
        if numRows == 1:
            return s
        else:        
            result = [[] for x in range(numRows)]       
                
            i = 0
            while len(s) > 0:              
                j = 0
                while j < numRows:
                    if i%(numRows - 1) == 0:
                        result[j].append(s[0])
                        s = s[1:]
                        
                        if len(s) == 0:
                            break
                        else:
                            j = j+1
                    else:
                        if j == numRows - 1 - i%(numRows - 1):
                            result[j].append(s[0])
                            s = s[1:]                        
                            if len(s) == 0:
                                break
                        j = j+1
                i = i+1
            
            "".join(result[0])
              
        
            for i in range(len(result)):
                result[i] = "".join(result[i])
                            
            return("".join(result))                
                        
              
        

        

s = "A"
numRows = 1
       
Solution.convert(1, "A", 1)



