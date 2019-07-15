# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        result=[]
        ll=len(array)
        if ll==1:
            return array[0]
        add_tmp=array[0]
        i=1
        maximum=add_tmp
        while i<ll:
            add_tmp+=array[i]
            if maximum<add_tmp:
                maximum=add_tmp
            while add_tmp>=0:
                i+=1
                add_tmp += array[i]
                if maximum<add_tmp:
                    maximum=add_tmp
                if i>=ll-1:
                    break
            result.append(maximum)
            add_tmp=0
            maximum=float("-inf")
            i+=1
        return max(result)

a=Solution()
b=a.FindGreatestSumOfSubArray([-2,-8,-1,-5,-9])
print(b)