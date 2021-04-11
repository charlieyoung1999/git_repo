# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:02:28 2021

@author: yanga
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        
        if len(s) == 0:
            temp_max = 0
            
        elif len(s) == 1:
            temp_max = 1
            
        else:
            temp_max = 1
            
            curr_head = 0
            curr_tail = 0
            
            
            while curr_tail < len(s) - 1:
                if not s[curr_tail + 1] in s[curr_head:(curr_tail + 1)]:
                    curr_tail = curr_tail + 1
                    temp_max = max(temp_max, curr_tail - curr_head + 1)
                else:
                    curr_head = s[curr_head:curr_tail+1].index(s[curr_tail + 1]) + curr_head + 1
                    if curr_tail < curr_head:
                        curr_tail = curr_head
            
        return temp_max

        
        
Solution.lengthOfLongestSubstring(1, "")            
        
        

        
        






