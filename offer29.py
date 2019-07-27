class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        for i in range(len(tinput)-1):
            for j in range(i+1,len(tinput)):
                if tinput[i]>tinput[j]:
                    tmp=tinput[j]
                    tinput[j]=tinput[i]
                    tinput[i]=tmp
        return tinput[0:k]






a=Solution()
tinput=[4,5,1,6,2,7,3,8]
k=4
b=a.GetLeastNumbers_Solution(tinput,k)
print(b)