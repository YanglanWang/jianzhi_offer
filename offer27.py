# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        result=[]
        if not ss:
            return result
        l1=list(ss)
        if len(l1)==1:
            return ss
        result.append(ss)
        for i in range(len(l1)):
            for j in range(len(l1)):
                tmp=l1[i]
                l1[i]=l1[j]
                l1[j]=tmp
                result_tmp=''.join(l1)
                l1 = list(ss)
                if result_tmp not in result:
                    result.append(result_tmp)
        result.sort()
        return result

a=Solution()
b=a.Permutation("abc")
print(b)