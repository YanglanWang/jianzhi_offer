# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # # write code here
        # dict_n={}
        # for i in duplication:
        #     if i in dict_n.keys():
        #         dict_n[i]+=1
        #     else:
        #         dict_n[i]=1
        # for i in range(len(duplication)):
        #     if dict_n[duplication[i]]>1:
        #         tmp=duplication[i]
        #         duplication[i]=duplication[0]
        #         duplication[0]=tmp
        #         return True,tmp
        # return False



        for i in range(len(numbers)):
            while numbers[i]!=i:
                if numbers[numbers[i]]==numbers[i]:
                    duplication[0]=numbers[i]
                    return duplication
                tmp=numbers[numbers[i]]
                numbers[numbers[i]]=numbers[i]
                numbers[i]=tmp

        return False

a=Solution()
b=a.duplicate([2,1,3,1,4],[4])
print(b)