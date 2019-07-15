# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        l=[1]
        l1=[2]
        l2=[3]
        l3=[5]
        while len(l)<index:
            min_num=min(l1+l2+l3)
            l.append(min_num)
            if min_num in l1:
                l1.remove(min_num)
            if min_num in l2:
                l2.remove(min_num)
            if min_num in l3:
                l3.remove(min_num)
            l1.append(min_num*2)
            l2.append(min_num*3)
            l3.append(min_num*5)
        return l[index-1]
a=Solution()
b=a.GetUglyNumber_Solution(4)
print(b)