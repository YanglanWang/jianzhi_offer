# -*- coding:utf-8 -*-
import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# class Solution:
#     # 返回对应节点TreeNode
#     nodeList=[]
#     def KthNode(self, pRoot, k):
#         # write code here
#         ll=self.getList(pRoot)
#         if k<=0 or k>len(ll):
#             return None
#         return ll[k-1]
#         #else:
#          #   return None
#     def getList(self,pRoot):
#         if pRoot.left==None and pRoot.right==None:
#             self.nodeList.append(pRoot)
#             return self.nodeList
#         self.getList(pRoot.left)
#         self.nodeList.append(pRoot)
#         self.getList(pRoot.right)
#         return self.nodeList

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 第三个节点是4
        # 前序遍历5324768
        # 中序遍历2345678
        # 后序遍历2436875
        # 所以是中序遍历，左根右
        global result
        result = []
        self.midnode(pRoot)
        if k <= 0 or len(result) < k:
            return None
        else:
            return result[k - 1]

    def midnode(self, root):
        if not root:
            return None
        self.midnode(root.left)
        result.append(root)
        self.midnode(root.right)


a=Solution()
pRoot=create_tree.fromList([8,6,10,5,7,9,11])
k=8
c=a.KthNode(pRoot,k)
print(c)