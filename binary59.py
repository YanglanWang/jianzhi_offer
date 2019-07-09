# -*- coding:utf-8 -*-
import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        nodeList1=[]
        nodeList2=[]
        nodeList_final=[]
        if pRoot==None:
            return None
        nodeList1=[pRoot]
        while len(nodeList1)!=0 or len(nodeList2)!=0:
            for i in nodeList1[::-1]:
                if i!=None:
                    nodeList_final.append(i.val)
                    nodeList1.remove(i)
                    nodeList2.extend([i.left,i.right])
            for i in nodeList2[::-1]:
                if i!=None:
                    nodeList_final.append(i.val)
                    nodeList2.remove(i)
                    nodeList1.extend([i.right,i.left])
        return nodeList_final

pRoot=create_tree.fromList([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
a=Solution()
print(a.Print(pRoot))