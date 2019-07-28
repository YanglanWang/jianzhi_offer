# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        # if len(s)==0:
        #     return 0
        # start=0
        # flag=True
        # if s[0]=="+" or s[0]=="-":
        #     start=1
        # if s[0]=="-":
        #     flag=False
        # num=0
        # s=s[start:]
        # for i in range(len(s)):
        #     if s[i]>='0' and s[i]<='9':
        #         num+=int(s[i])*(pow(10,len(s)-i-1))
        #     else:
        #         num=0
        #         break
        # if flag==False:
        #     num=-num
        # return num
























        fuhao=0
        if s[0]=='+' or s[0]=='-':
            fuhao=s[0]
            s=s[1:]

        for i in s:
            if not ('0'<=i and i<='9'):
                return False
        num=int(s)
        if fuhao!=0:
            num=-num if fuhao=='-' else num
        return num








a=Solution()
b=a.StrToInt('+133')
print(b)