class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        list_n=[]
        list_m=[]
        for i in range(len(array)-1):
            for j in range(i+1,len(array)):
                if array[i]+array[j]==tsum:
                    list_n.append([array[i],array[j]])
                    list_m.append(array[i]*array[j])
        if len(list_n)==0:
            return[]
        else:

            min_index=list_m.index(min(list_m))
            return list_n[min_index]

a=Solution()
b=a.FindNumbersWithSum([1,2,4,7,11,16],10)
print(b)
c=[2,3,1,4]
