# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 00:07:49 2021

@author: yanga
"""

# merge sort
import math

def merge_sort(temp_list):
    sub_1 = temp_list[:math.floor(len(temp_list)/2)]
    sub_2 = temp_list[math.floor(len(temp_list)/2):]
    
    # sort step
    if len(sub_1) > 1:
        sub_1 = merge_sort(sub_1)
    if len(sub_2) > 1:
        sub_2 = merge_sort(sub_2)
    
    # merge step
    merged_list = []
    
    while ((len(sub_1) > 0) and (len(sub_2) > 0)):
        if(sub_1[0] < sub_2[0]):
            merged_list.append(sub_1[0])
            del sub_1[0]
        else:
            merged_list.append(sub_2[0])
            del sub_2[0]                   
    
    if len(sub_1) > 0:
        merged_list.extend(sub_1)
    if len(sub_2) > 0:
        merged_list.extend(sub_2)
        
    return(merged_list)
            
            
temp_list = [2,3,5,9,1,8,7,6]
temp_list = [1,4,4,2]
merge_sort(temp_list)
            
            




