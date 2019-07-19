# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count = 0
        # if n<0:
        #     n = n & 0xffffffff
        while n:
            count += 1
            n = n & (n-1)
        return count

        # l=[]
        # for i in range(16):
        #     l.append(n >> i & 1)

        # l=[ for i in range(0, 32)]
        return sum(l)




a=Solution()
b=a.NumberOf1(-4)
print(b)