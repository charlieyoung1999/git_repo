# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 00:25:45 2021

@author: yanga
"""

import os
import re


### pratice of counting inversions

def count_invertions_and_sort(temp_imput):
    
    # separate list into two
    mid_index = len(temp_imput)//2
    sub_1 = temp_imput[:mid_index]
    sub_2 = temp_imput[mid_index:]
    
    
    # inversions of left part
    if len(sub_1) > 1:
        temp = count_invertions_and_sort(sub_1)
        num_inv_1 = temp[0]
        sub_1 = temp[1]
    else:
        num_inv_1 = 0
    
    # inversions of right part    
    if len(sub_2) > 1:
        temp = count_invertions_and_sort(sub_2)
        num_inv_2 = temp[0]
        sub_2 = temp[1]
    else:
        num_inv_2 = 0
        
    # split inversions
    combined_list = []
    total_inv = 0
    
    while len(sub_1) > 0 and len(sub_2) > 0:
        if sub_2[0] < sub_1[0]:
            combined_list.append(sub_2[0])
            total_inv = total_inv + len(sub_1)
            del sub_2[0]
        else:
            combined_list.append(sub_1[0])
            del sub_1[0]
        
    if len(sub_1) > 0:
        combined_list.extend(sub_1)
    if len(sub_2) > 0:
        combined_list.extend(sub_2)
        
    total_inv = total_inv + num_inv_1 + num_inv_2
    
    return [total_inv, combined_list]
        
    
# load in data
os.getcwd()

with open('C:\\git_repo\\python_scratches\\count_inversions_num_array.txt', 'r') as f:
    lines = f.readlines()
    
    
def convert_to_int(temp):
    temp = re.sub("\n", "", temp)
    temp = int(temp)
    return temp
    
target_imput = list(map(convert_to_int, lines))

    
prob_solution = count_invertions_and_sort(target_imput)
prob_solution = prob_solution[0]
prob_solution





















