# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s)==0:
            return 0
        start=0
        flag=True
        if s[0]=="+" or s[0]=="-":
            start=1
        if s[0]=="-":
            flag=False
        num=0
        s=s[start:]
        for i in range(len(s)):
            if s[i]>='0' and s[i]<='9':
                num+=int(s[i])*(pow(10,len(s)-i-1))
            else:
                num=0
                break
        if flag==False:
            num=-num
        return num

a=Solution()
b=a.StrToInt('1a33')
print(b)