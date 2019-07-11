# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dict_n={}
        for i in duplication:
            if i in dict_n.keys():
                dict_n[i]+=1
            else:
                dict_n[i]=1
        for i in range(len(duplication)):
            if dict_n[duplication[i]]>1:
                tmp=duplication[i]
                duplication[i]=duplication[0]
                duplication[0]=tmp
                return True,tmp
        return False

a=Solution()
b=a.duplicate(5,[2,1,3,1,4])
print(b)