# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 23:19:23 2021

@author: yanga
"""

class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        else:
            i = 0
            j = len(nums)-1
            
            while i <= j:
                if nums[i] == val:
                    while nums[j] == val and j >= 0:
                        j = j-1
                    if j < 0:
                        return 0
                    elif j < i:
                        break
                    else:
                        nums[i], nums[j] = nums[j], nums[i]
                        j = j-1
                    
                i = i+1
                
            return i
        


Solution.removeElement(1, [4,5], 5)
     
        
        
