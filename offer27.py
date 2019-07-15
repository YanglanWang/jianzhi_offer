# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        ll=[]
        if not ss:
            return ll
        if len(ss)==1:
            return ss
        return self.circle(ss)


    def circle(self,ss):
        if len(ss)==2:
            if ss!=ss[::-1]:
                return [ss,ss[::-1]]
            else:
                return [ss]
        l_tmp=[]
        for j in range(len(ss)):
            for i in self.circle(ss[0:j]+ss[j+1:]):
                l_=ss[j]+i
                if l_ not in l_tmp:
                    l_tmp.append(l_)
                # result_tmp=''.join(i)
        return l_tmp

a=Solution()
b=a.Permutation("aa")
print(b)