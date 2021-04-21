# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 22:25:56 2021

@author: yanga
"""

class Solution:
    def isAnagram(self, s, t):
        if(len(s) == len(t)):
            s = s.lower()
            t = t.lower()
            
            temp1 = [0]*26
            temp2 = [0]*26
            
            for i in range(len(s)):
                temp1[ord(s[i]) - ord("a")] += 1
                
            for j in range(len(s)):
                temp2[ord(t[j]) - ord("a")] += 1
                
            k = 0
            while k < 26:
                if temp1[k] != temp2[k]:
                    return False
                else:
                    k += 1
            
            return True
        
        else:
            return False
        
        





ord("a")
ord("z") - ord("a")


s = "whatisthis"


