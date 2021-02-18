# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:26:07 2021

@author: yanga
"""

class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        else:
            x = [i+j for i,j in enumerate(nums[:-1])]
            x1 = list(map(lambda k: k >= len(x), x))
            
            if x1[0]:
                return True
            elif not any(x1):
                return False
            else:
                temp_list = []
                for i in range(len(x1)):
                    if x1[i]:
                        temp_list.append(nums[:(i+1)])
                return any(list(map(self.canJump, temp_list)))
            
        
        
        
# backtrack method, exceeds time limit
def canJump(nums):
    if len(nums) == 1:
        return True
    else:
        x = [i+j for i,j in enumerate(nums[:-1])]
        x1 = list(map(lambda k: k >= len(x), x))
        
        if x1[0]:
            return True
        elif not any(x1):
            return False
        else:
            temp_list = []
            for i in range(len(x1)):
                if x1[i]:
                    temp_list.append(nums[:(i+1)])
            return any(list(map(canJump, temp_list)))


# solution 2
def canJump(nums): 
    if len(nums) == 1:
        return True
    else:
        far_index = 0
        i = 0
        
        output = False
    
        while i <= far_index:
            if i+nums[i] > far_index:
                far_index = i+nums[i]
                if far_index >= (len(nums)-1):
                    output = True
                    break
            i = i+1
        
        return output















