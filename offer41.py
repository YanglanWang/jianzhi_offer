class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        list_n=[]
        for i in range(1,tsum):
            for j in range(2,tsum):
                if sum(range(i,i+j))==tsum:
                    list_n.append(range(i,i+j))
        return list_n

a=Solution()
b=a.FindContinuousSequence(15)
print(b)