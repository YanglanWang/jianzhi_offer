# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return None
        low = 0
        high = len(rotateArray)-1
        medium = int((low+high) / 2)
        if rotateArray[medium]>rotateArray[high]:
            low=medium
            medium=int((low+high)/2)
        else:
            
