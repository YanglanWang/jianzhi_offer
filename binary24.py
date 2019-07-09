import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def FindPath(self, root, expectNumber):
        # write code here
        start=root
        if start==None:
            return []
        if start.left==None and start.right==None and start.val==expectNumber:
            return [[start.val]]
        leftpath=self.FindPath(start.left,expectNumber-start.val)
        rightpath=self.FindPath(start.right,expectNumber-start.val)
        for i in leftpath+rightpath:
            i=i.insert(0,start.val)
        return leftpath+rightpath

a=Solution()
root=create_tree.fromList([10,5,12,4,7])
a.FindPath(root,22)