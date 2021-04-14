# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 00:05:31 2021

@author: yanga
"""

class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        elif len(haystack) < len(needle):
            return -1
        elif len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        else:
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i] == needle[0]:
                    if len(needle) == 1:
                        return i
                    else:
                        check = True
                        for j in range(1,len(needle)):
                            if haystack[i+j] != needle[j]:
                                check = False
                                break
                        
                        if check == True:
                            return i
                
            return -1
                        
      


Solution.strStr(1, "abc", "c")










