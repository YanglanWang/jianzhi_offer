class Solution:
    def reOrderArray(self, array):
        # write code here
        for i in range(len(array)-1):
            if array[i]%2==0 and array[i+1]%2==1:
                a=array[i+1]
                array[i+1]=array[i]
                array[i]=a
                j=i-1
                while j>=0 and array[j]%2==0:
                    b=array[j+1]
                    array[j+1]=array[j]
                    array[j]=b
                    j=j-1
        return array
a=Solution()
print(a.reOrderArray([2,4,6,1,3,5,7]))