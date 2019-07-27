import create_tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        if pRoot==None:
            return 0
        if pRoot.left==None and pRoot.right==None:
            return 1
        return max(1+self.TreeDepth(pRoot.left),1+self.TreeDepth(pRoot.right))





a=Solution()
b=create_tree.fromList([1,2,3,4,5,6,7,8])
c=a.TreeDepth(b)
print(c)