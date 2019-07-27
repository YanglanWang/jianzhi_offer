class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        ll=len(numbers)//2
        dict_n={}
        for i in numbers:
            if i in dict_n.keys():
                dict_n[i]+=1
            else:
                dict_n[i]=1
        result=[]
        for key in dict_n.keys():
            if dict_n[key]>ll:
                result.append(key)
        if len(result)==0:
            return 0
        else:
            return result

a=Solution()
b=a.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2])
print(b)