# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 00:16:10 2021

@author: yanga
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        
        start_point = 0
        valid_start = True
        
        while start_point < len(s) - 1:
            if s[start_point] == " ":
                start_point += 1
                valid_start = True
            else:
                if valid_start is True:                    
                    left = start_point
                    right = start_point
                    
                    while right <= len(s) - 1:
                        if s[right] == " ":
                            break
                        else:
                            right += 1
                            
                    right -= 1
                
                    
                    while left < right:
                        s[left], s[right] = s[right], s[left]
                        left += 1
                        right -= 1
                    
                    valid_start = False
                
                start_point += 1
                
        return "".join(s)
        
        
a = Solution()
a.reverseWords("this is for testing")
s = "this is for testing"


# simple solution
" ".join([i[::-1] for i in s.split()])
