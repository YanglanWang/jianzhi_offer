import create_tree
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

#------这种做法pycharm没问题 牛客有问题
# class Solution:
#     def HasSubtree(self,pRoot1,pRoot2):
#         if not pRoot1 or not pRoot2:
#             return False
#
#         return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2) or self.IsSubtree(pRoot1,pRoot2)
#
#     def IsSubtree(self,pRoot1,pRoot2):
#         if pRoot1==None or pRoot2==None:
#             return True
#         if pRoot1.val==pRoot2.val:
#             return self.IsSubtree(pRoot1.left,pRoot2.left) and self.IsSubtree(pRoot1.right,pRoot2.right)
#         else:
#             return False

#----niuke 能通过
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2) or self.is_subtree(pRoot1, pRoot2)
    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)

a=Solution()
A=create_tree.fromList([8,None,8,None,9,None,2,None,5])
B=create_tree.fromList([8,None,9,3,2])
c=a.HasSubtree(A,B)
print(c)



