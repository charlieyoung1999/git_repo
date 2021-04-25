# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:34:18 2021

@author: yanga
"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def print_all_nodes(self):
        temp = self
        while temp:
            print(temp.val)
            temp = temp.next
        
    def import_string(self, temp_num:int):
        temp_num = list(str(temp_num))
        
        temp_node = ListNode(temp_num[-1])
        
        if len(temp_num) > 1:
            i = len(temp_num) - 2
            while i >= 0:
                temp_head = ListNode(temp_num[i], temp_node)
                temp_node = temp_head
                i -= 1
        
        self.val = temp_node.val
        self.next = temp_node.next
        
            
        



