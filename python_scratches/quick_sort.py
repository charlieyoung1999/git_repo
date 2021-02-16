# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:15:58 2021

@author: yanga
"""

# a practice of quick sort
# the option 3 does not reach correction solution yet

def quick_sort(temp_imput, pivot_option):
    temp_list = [x for x in temp_imput]
    comparison_count = 0
    
    if len(temp_list) > 1:    
        if pivot_option == 2:
            temp_list[0], temp_list[-1] = temp_list[-1], temp_list[0]
        
        if pivot_option == 3:       
            case_1 = (temp_list[len(temp_list)//2-1] > temp_list[0]) and (temp_list[len(temp_list)//2-1] < temp_list[-1])
            case_2 = (temp_list[len(temp_list)//2-1] < temp_list[0]) and (temp_list[len(temp_list)//2-1] > temp_list[-1])
            case_3 = (temp_list[-1] > temp_list[len(temp_list)//2-1]) and (temp_list[-1] < temp_list[0])
            case_4 = (temp_list[-1] < temp_list[len(temp_list)//2-1]) and (temp_list[-1] > temp_list[0])
            
            if case_1 or case_2:
                temp_list[0], temp_list[len(temp_list)//2-1] = temp_list[len(temp_list)//2-1], temp_list[0]
            if case_3 or case_4:
                temp_list[0], temp_list[-1] = temp_list[-1], temp_list[0]
    
        i = 0
        j = 1
        while j < len(temp_list):
            if temp_list[j] < temp_list[0]:
                temp_list[j], temp_list[i+1] = temp_list[i+1], temp_list[j]
                j = j+1
                i = i+1
            else:
                j = j+1
        
        
        comparison_count = comparison_count + len(temp_list) - 1
        
        if i > 0:
            temp_list[0], temp_list[i] = temp_list[i], temp_list[0]
            temp_out = quick_sort(temp_list[:i], pivot_option)
            temp_list[:i] = temp_out[0]
            comparison_count = comparison_count + temp_out[1]
        if len(temp_list) > i+1:
            temp_out = quick_sort(temp_list[(i+1):], pivot_option)
            temp_list[(i+1):] = temp_out[0]
            comparison_count = comparison_count + temp_out[1]
        
    return [temp_list, comparison_count]







with open('C:\\git_repo\\python_scratches\\quicksort_num_array.txt') as f:
    target_imput = [int(x) for x in f]  


prob_solution = quick_sort(target_imput, 1)
prob_solution = prob_solution[1]
print(prob_solution)

prob_solution = quick_sort(target_imput, 2)
prob_solution = prob_solution[1]
print(prob_solution)

prob_solution = quick_sort(target_imput, 3)
prob_solution = prob_solution[1]
print(prob_solution)









