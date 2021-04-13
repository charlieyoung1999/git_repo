# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:41:00 2021

@author: yanga
"""

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            i = 0
            j = 1
            
            for j in range(1, len(nums)):
                if nums[i] != nums[j]:
                    i = i+1
                    nums[i] = nums[j]
            
            return i+1
           


nums = [1,1,2]
Solution.removeDuplicates(1, nums)


