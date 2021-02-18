# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:34:23 2021

@author: yanga
"""


class Solution:
    def isValid(self, s):
        temp = []
        for x in s:
            if len(temp) == 0:
                temp.append(x)
            else:
                if (temp[-1] == "(" and x == ")") or (temp[-1] == "[" and x == "]") or (temp[-1] == "{" and x == "}"):
                    temp.pop()
                else:
                    temp.append(x)
        return(len(temp) == 0)
                    
        
        
        
        
s = "([)]"        
Solution.isValid(1,s)


     
