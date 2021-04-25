# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 23:45:47 2021

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
        temp_num = [int(x) for x in list(str(temp_num))]
        temp_node = None
        while temp_num:
            temp_node = ListNode(temp_num.pop(), temp_node)
            
        self.val = temp_node.val
        self.next = temp_node.next 
            
            
            
        
        
        

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        curr_node = ListNode(0)
        ListHead = curr_node
        
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr_node.next = ListNode(carry%10)
            curr_node = curr_node.next
            carry = carry//10
        
        ListHead = ListHead.next
        
        return ListHead
       








