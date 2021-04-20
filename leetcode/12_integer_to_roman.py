# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:32:46 2021

@author: yanga
"""



class Solution:
    def intToRoman(self, num):
        
        if num >= 1 and num <= 3999:
            
            num = list(str(num))
            roman = ""
            
            digit = 1   
            
            while len(num) > 0:
                temp = num.pop()
                temp = int(temp)
                
                if digit == 1:
                    if temp >= 1 and temp <= 3:
                        roman = "I"*temp + roman
                    elif temp == 4:
                        roman = "IV" + roman
                    elif temp == 5:
                        roman = "V" + roman
                    elif temp >= 6 and temp <= 8:
                        roman = "V" + "I"*(temp-5) + roman
                    elif temp == 9:
                        roman = "IX" + roman
                    else:
                        pass
                    
                elif digit == 2:
                    if temp >= 1 and temp <= 3:
                        roman = "X"*temp + roman
                    elif temp == 4:
                        roman = "XL" + roman
                    elif temp == 5:
                        roman = "L" + roman
                    elif temp >= 6 and temp <= 8:
                        roman = "L" + "X"*(temp-5) + roman
                    elif temp == 9:
                        roman = "XC" + roman
                    else:
                        pass
                
                elif digit == 3:
                    if temp >= 1 and temp <= 3:
                        roman = "C"*temp + roman
                    elif temp == 4:
                        roman = "CD" + roman
                    elif temp == 5:
                        roman = "D" + roman
                    elif temp >= 6 and temp <= 8:
                        roman = "D" + "C"*(temp-5) + roman
                    elif temp == 9:
                        roman = "CM" + roman
                    else:
                        pass
                
                else:
                    roman = "M"*temp + roman
                
                digit += 1
            
            return roman
                
        else:
            return "ERROR"
            
                
                


a = Solution()
a.intToRoman(10)




num = 10




