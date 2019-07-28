import create_tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.subBalance(pRoot)[1]
    def subBalance(self,pRoot):
        if pRoot==None:
            return 0,True

        left_len,left_flag=self.subBalance(pRoot.left)
        right_len,right_flag=self.subBalance(pRoot.right)
        if abs(left_len-right_len)<=1:
            return max(left_len+1,right_len+1), left_flag and right_flag
        else:
            return max(left_len+1,right_len+1), False




a=Solution()
b=create_tree.fromList([5,4,None,3,None])
c=a.IsBalanced_Solution(b)
print(c)