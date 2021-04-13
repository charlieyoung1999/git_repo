# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:21:21 2021

@author: yanga
"""


class Solution:
    def romanToInt(self, s):        
        s = s[::-1]
        temp = 0  
        
        while len(s) > 0:
            check = False
            temp1 = 0
            
            if len(s) > 1:
                if s[:2] == "VI":
                    temp1 = 4
                    check = True                    
                if s[:2] == "XI":
                    temp1 = 9
                    check = True
                if s[:2] == "LX":
                    temp1 = 40
                    check = True
                if s[:2] == "CX":
                    temp1 = 90
                    check = True
                if s[:2] == "DC":
                    temp1 = 400
                    check = True
                if s[:2] == "MC":
                    temp1 = 900
                    check = True
                
            if check:
                temp = temp + temp1
                s = s[2:]
            else:
                if s[0] == "I":
                    temp = temp + 1
                elif s[0] == "V":
                    temp = temp + 5
                elif s[0] == "X":
                    temp = temp + 10
                elif s[0] == "L":
                    temp = temp + 50
                elif s[0] == "C":
                    temp = temp + 100
                elif s[0] == "D":
                    temp = temp + 500
                else:
                    temp = temp + 1000
                
                s = s[1:]
            
        return temp



Solution.romanToInt(1, "MCMXCIV")



































