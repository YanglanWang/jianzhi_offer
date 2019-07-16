# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if len(A)==0:
            return None
        C=[]
        D=[]
        B=[]
        C.append(A[0])
        for i in range(1,len(A)-1):
            C.append(C[i-1]*A[i])
        D.append(A[-1])
        for i in range(len(A)-2,0,-1):
            D.append(D[len(A)-i-2]*A[i])
        D.reverse()
        B.append(D[0])
        for i in range(1,len(A)-1):
            B.append(C[i-1]*D[i])
        B.append(C[-1])
        return B

a=Solution()
b=a.multiply([1,2,3,4,5])
print(b)