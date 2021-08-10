# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 02:22:02 2021

@author: yanga
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]




s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

list(range(1, len(s) + 1))
list(range(2))
s[1:2]
