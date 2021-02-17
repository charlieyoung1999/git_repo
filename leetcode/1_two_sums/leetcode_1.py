# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:31:55 2021

@author: yanga
"""

class Solution:
    def twoSum(self, nums, target):
        
        checked_items = {}
        
        i = 0
        temp_1 = True
        
        while i < len(nums):
            if target - nums[i] in checked_items:
                temp_1 = False
                return [checked_items[target - nums[i]], i]
            else:
                checked_items[nums[i]] = i
                i = i+1
                
        if temp_1:
            print("no solution found!\n")
            return[-1,-1]
            

Solution.twoSum(1, [1,2,3], 5)


