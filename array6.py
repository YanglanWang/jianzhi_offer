# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return None

        # low=0
        # high=len(rotateArray)-1
        # while high-low!=1:
        #     medium=int((low+high)/2)
        #     if rotateArray[low]<rotateArray[medium]:
        #         low=medium
        #     else:
        #         high=medium
        # return rotateArray[high]
        mini=1e-10
        for i in rotateArray:
            if i<mini:
                return i
            mini=i
        return rotateArray[0]

a=Solution()
b=a.minNumberInRotateArray([1,1,1,0,1])
print(b)



# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.ll=[]
    def Insert(self, num):
        # write code here
        self.ll.append(num)
    def GetMedian(self,ll):
        # write code here
        self.ll.sort()
        if len(self.ll)%2==0:
            return float((self.ll[len(self.ll)/2-1]+self.ll[len(self.ll)/2])/2)
        else:
            return float(self.ll[int(len(self.ll)/2)])