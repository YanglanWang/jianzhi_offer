# # -*- coding:utf-8 -*-
# class Solution:
#     def FindGreatestSumOfSubArray(self, array):
#         # write code here
#         result=[]
#         ll=len(array)
#         if ll==1:
#             return array[0]
#         add_tmp=array[0]
#         i=1
#         maximum=add_tmp
#         while i<ll:
#             add_tmp+=array[i]
#             if maximum<add_tmp:
#                 maximum=add_tmp
#             while add_tmp>=0:
#                 i+=1
#                 add_tmp += array[i]
#                 if maximum<add_tmp:
#                     maximum=add_tmp
#                 if i>=ll-1:
#                     break
#             result.append(maximum)
#             add_tmp=0
#             maximum=float("-inf")
#             i+=1
#         return max(result)

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        start=0
        ll=[]
        while start<len(array):
            t = 0
            for i in range(start,len(array)):
                t+=array[i]
                if t<0:
                    start=i+1
                    break
                if t>t-array[i]:
                    ll.append(t)
            if i == len(array) - 1:
                break
        if len(ll)==0:
            return max(array)
        return max(ll)

a=Solution()
b=a.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5])
print(b)