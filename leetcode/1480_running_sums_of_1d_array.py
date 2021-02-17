# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 23:17:29 2021

@author: yanga
"""


class Solution:
    def runningSum(self, nums):
        output = []
        for i in nums:
            if len(output) == 0:
                output.append(i)
            else:
                output.append(output[len(output)-1] + i)
        return output
            


class Solution2:
    def runningSum(self, nums):
        for x in range(1,len(nums)):
            nums[x] = nums[x] + nums[x-1]
        return nums
            
            
