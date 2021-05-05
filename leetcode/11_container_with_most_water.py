# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:31:48 2021

@author: yanga
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_1 = 0
        pointer_2 = len(height) - 1
        
        max_area = 0
        
        while pointer_1 < pointer_2:
            temp_area = (pointer_2 - pointer_1)*min(height[pointer_1], height[pointer_2])
            if temp_area > max_area:
                max_area = temp_area
            
            if height[pointer_1] <= height[pointer_2]:
                pointer_1 += 1
            else:
                pointer_2 -= 1
            
        return max_area
            
            
        









height = [1,8,6,2,5,4,8,3,7]

a = Solution()
a.maxArea(height)

