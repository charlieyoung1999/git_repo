# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:57:03 2021

@author: yanga
"""

from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pointer_1 = 0
        pointer_2 = len(nums) - 1
        
        temp_out = -1
        
        while pointer_1 <= pointer_2:
            pivot = (pointer_1 + pointer_2)//2
            
            if nums[pivot] < target:
                pointer_1 = pivot + 1
            elif nums[pivot] > target:
                pointer_2 = pivot - 1
            else:
                temp_out = pivot
                break
        
        print(pivot)
            
        return temp_out
            
a = Solution()
a.search([-1,0,3,5,9,12], 9)


