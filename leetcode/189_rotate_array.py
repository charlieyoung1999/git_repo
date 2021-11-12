# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 23:32:39 2021

@author: yanga
"""


from typing import List 


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n
        
        loop_start = 0
        total_count = 0
        
        while total_count < n:
            curr_node = loop_start
            curr_value = nums[curr_node]

            while True:
                next_node = (curr_node + k)%n
                
                nums[next_node], curr_value = curr_value, nums[next_node]
                total_count += 1
                curr_node = next_node 
                
                if curr_node == loop_start:
                    break
                
            loop_start += 1
        
        return nums
    
    
    
a = Solution()
a.rotate([-1,-100,3,99], 2)
        