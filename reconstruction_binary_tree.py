class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        root=TreeNode(pre[0])
        i=tin.index(root.val)
        self.left=self.reConstructBinaryTree(pre[1:1+i],tin[:i])
        self.right=self.reConstructBinaryTree(pre[1+i:],tin[1+i:])
        return root


a=Solution()
a.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])