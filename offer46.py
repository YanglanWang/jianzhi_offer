class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        list_origin=range(n)
        i=0
        while len(list_origin)>1:
            list_sing = []
            for i in range(len(list_origin)):
                if (i+1)%3==0:
                    list_sing.append(list_origin[i])
            list_origin=[i for i in list_origin if i not in list_sing]
        return list_origin[0]

a=Solution()
b=a.LastRemaining_Solution(5,3)
print(b)