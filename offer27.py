# -*- coding:utf-8 -*-
class Solution:
    # def Permutation(self, ss):
    #     # write code here
    #     ll=[]
    #     if not ss:
    #         return ll
    #     if len(ss)==1:
    #         return ss
    #     return self.circle(ss)
    #
    #
    # def circle(self,ss):
    #     if len(ss)==2:
    #         if ss!=ss[::-1]:
    #             return [ss,ss[::-1]]
    #         else:
    #             return [ss]
    #     l_tmp=[]
    #     for j in range(len(ss)):
    #         for i in self.circle(ss[0:j]+ss[j+1:]):
    #             l_=ss[j]+i
    #             if l_ not in l_tmp:
    #                 l_tmp.append(l_)
    #             # result_tmp=''.join(i)
    #     return l_tmp


    def Permutation(self, ss):
        tmp = []
        if len(ss)<=0:
            return []
        if len(ss)==1:
            return [ss]
        for i in range(len(ss)):
            t=self.Permutation(ss[0:i]+ss[i+1:])
            for j in range(len(t)):
                tmp.append(ss[i]+t[j])
        tmp=list(set(tmp))
        tmp.sort()
        return tmp

a=Solution()
b=a.Permutation("abc")
print(b)