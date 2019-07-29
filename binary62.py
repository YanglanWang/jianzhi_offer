# -*- coding:utf-8 -*-
import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    # nodeList=[]
    # def KthNode(self, pRoot, k):
    #     # write code here
    #     self.getList(pRoot)
    #     ll =self.nodeList
    #     if k<=0 or k>len(ll):
    #         return None
    #     return ll[k-1]
    #     #else:
    #      #   return None
    # def getList(self,pRoot):
    #     if pRoot.left==None and pRoot.right==None:
    #         self.nodeList.append(pRoot)
    #         # return self.nodeList
    #         return None
    #     self.getList(pRoot.left)
    #     self.nodeList.append(pRoot)
    #     self.getList(pRoot.right)
    #     # return self.nodeList

    def KthNode(self, pRoot, k):
        l_list=self.Getlist(pRoot)
        if k>=len(l_list):
            return None
        return l_list[k]



    def Getlist(self,pRoot):
        if pRoot==None:
            return []
        if pRoot.left==None and pRoot.right==None:
            return [pRoot]
        return self.Getlist(pRoot.left)+[pRoot]+self.Getlist(pRoot.right)


a=Solution()
pRoot=create_tree.fromList([8,6,10,5,None,9,11])
k=8
c=a.KthNode(pRoot,k)
print(c)