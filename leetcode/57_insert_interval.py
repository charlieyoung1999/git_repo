# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 00:59:37 2021

@author: yanga
"""


class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        elif newInterval[1] < intervals[0][0]:
            intervals.insert(0,newInterval)
            return intervals
        elif newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        else:
            insert_place = 0
            
            for i in range(len(intervals)):
                if intervals[i][0] <= newInterval[0]:
                    if i != len(intervals) - 1:
                        if intervals[i+1][0] > newInterval[0]:
                            if intervals[i][1] < newInterval[0]:
                                insert_place = i+1
                            else:
                                insert_place = i
                    else:
                        if intervals[i][1] < newInterval[0]:
                            insert_place = i+1
                        else:
                            insert_place = i
            
            end_interval = len(intervals) - 1
            for j in range(insert_place, len(intervals)-1):
                if intervals[j][1] >= newInterval[1] or intervals[j+1][0] > newInterval[1]:
                    end_interval = j
                    break
                
            if newInterval[1] < intervals[insert_place][0]:
                intervals.insert(insert_place, newInterval)
            else:
                new_left = min(intervals[insert_place][0], newInterval[0])
                new_right = max(intervals[end_interval][1], newInterval[1])
            
                del intervals[insert_place:(end_interval+1)]
                intervals.insert(insert_place, [new_left, new_right])
            
            return intervals
            
       

Solution.insert(1, [[1,3],[6,9]], [2,5])

            
                
            

























