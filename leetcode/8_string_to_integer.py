# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:05:31 2021

@author: yanga
"""

class Solution:    
    def myAtoi(self, s):
        s = s.lstrip()
        
        if len(s) == 0:
            return 0
        else:
            sign = "positive"
            
            if len(s) > 1:
                temp_sign = s[0]
                
                if temp_sign == "-":
                    sign = "negative"
                    s = s[1:]
                elif temp_sign == "+":
                    sign = "positive"
                    s = s[1:]
                else:
                    sign = "positive"
                  
            import re
            re_check = re.search("^\d+", s)
            
            if re_check:
                s = re_check.group(0)
                s = int(s)
            else:
                s = 0
            
            if sign == "negative":
                s = 0-s
                
            if s < -2**31:
                s = -2**31
            elif s > 2**31 - 1:
                s = 2**31 - 1
            else:
                pass
            
            return s
            
               

             
                
a = Solution()
a.myAtoi("words and 987")       
