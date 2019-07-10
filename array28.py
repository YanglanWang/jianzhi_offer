class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        times=len(numbers)
        dict_n={}
        out=[]
        for i in numbers:
            if i in dict_n:
                dict_n[i]+=1
            else:
                dict_n[i]=1
        for i in dict_n.keys():
            if dict_n[i]>times/2:
                return i
                out.append(i)
        if len(out)==0:
            return None

a=Solution()
numbers=[1, 2, 3, 2, 4, 2, 5, 2, 3]
b=a.MoreThanHalfNum_Solution(numbers)
print(b)