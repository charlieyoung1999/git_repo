# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:40:37 2021

@author: yanga
"""


class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        return len(s.split(" ")[-1])








