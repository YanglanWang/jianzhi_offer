import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # def Convert(self, pRootOfTree):
    #     # write code here
    #     if pRootOfTree==None:
    #         return None
    #     a=self.conver_tmp(pRootOfTree)
    #     while a.left!=None:
    #         a=a.left
    #     return a
    #
    #
    # def conver_tmp(self,pRootOfTree):
    #     if pRootOfTree.left==None and pRootOfTree.right==None:
    #         return pRootOfTree
    #     if pRootOfTree.left!=None:
    #         left_tmp=self.conver_tmp(pRootOfTree.left)
    #         while left_tmp.right!=None:
    #             left_tmp=left_tmp.right
    #         pRootOfTree.left=left_tmp
    #         left_tmp.right=pRootOfTree
    #     if pRootOfTree.right!=None:
    #         right_tmp=self.conver_tmp(pRootOfTree.right)
    #         while right_tmp.left!=None:
    #             right_tmp=right_tmp.left
    #         pRootOfTree.right=right_tmp
    #         right_tmp.left=pRootOfTree
    #
    #     return pRootOfTree


    def Convert(self, pRootOfTree):

        if pRootOfTree.left==None and pRootOfTree.right==None:
            return pRootOfTree
        if pRootOfTree.left!=None:
            self.Convert(pRootOfTree.left)
            a=pRootOfTree.left
            while a.right!=None:
                a=a.right
            pRootOfTree.left=a
            a.right=pRootOfTree

        if pRootOfTree.right!=None:
            self.Convert(pRootOfTree.right)
            b=pRootOfTree.right
            while b.left!=None:
                b=b.left
            pRootOfTree.right=b
            b.left=pRootOfTree
        while pRootOfTree.left!=None:
            pRootOfTree=pRootOfTree.left
        return pRootOfTree

a=Solution()
# pRootOfTree=create_tree.fromList([5,4,None,3,None,None,None,2,None,1,None])
pRootOfTree=create_tree.fromList([5,4,None,3,None,None,None,2,None,None,None,None,None,None,None,1])
c=a.Convert(pRootOfTree)
print(c)