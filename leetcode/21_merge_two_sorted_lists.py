# -*- coding: utf-8 -*-
"""
Created on Sat May  1 23:45:10 2021

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
        


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        
        temp = new_list = ListNode(0)
        
        while head1 or head2:
            if head1 and head2:
                if head2.val <= head1.val:
                    new_list.next = ListNode(head2.val)
                    new_list = new_list.next
                    head2 = head2.next
                else:
                    new_list.next = ListNode(head1.val)
                    new_list = new_list.next
                    head1 = head1.next
            elif head1:
                new_list.next = ListNode(head1.val)
                new_list = new_list.next
                head1 = head1.next
            else:
                new_list.next = ListNode(head2.val)
                new_list = new_list.next
                head2 = head2.next
            
        return temp.next
                
        
        


