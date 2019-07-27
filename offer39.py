import create_tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot==None:
            return 0,True
        left_len=self.TreeDepth(pRoot.left)+1
        right_len=1+self.TreeDepth(pRoot.right)
        if abs(left_len-right_len)>1:
            return max(left_len,right_len),False
        return



a=Solution()
b=create_tree.fromList([1,2,3,4,5,6,7,8])
c=a.TreeDepth(b)
print(c)