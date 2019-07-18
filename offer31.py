# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        i=1
        length=len(str(n))
        weishu=pow(10,i)
        result=0
        while i<=length:
            a=n//weishu
            b=n%weishu
            xishu=pow(10,i-1)
            result+=xishu*a
            if b<xishu:
                result+=0
            elif b>xishu*2-1:
                result+=xishu
            else:
                result+=b-xishu+1
            i+=1
            weishu=pow(10,i)
        return result

a=Solution()
b=a.NumberOf1Between1AndN_Solution(1)
print(b)