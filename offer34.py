class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s)==0:
            return -1
        dict_n={}
        for i in s:
            if i not in dict_n:
                dict_n[i]=1
            else:
                dict_n[i]+=1
        for i in s:
            if dict_n[i]==1:
                return s.index(i)
        if i==len(dict_n.keys()):
            return -1

a=Solution()
b=a.FirstNotRepeatingChar('google')
print(b)