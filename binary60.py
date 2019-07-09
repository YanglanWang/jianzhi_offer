# -*- coding:utf-8 -*-
import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        nodelist_final=[]
        nodeList=[pRoot]
        node_tmp=[]
        node_val_tmp=[]
        while len(nodeList)!=0:
            for i in nodeList:
                node_val_tmp.append(i.val)
                if i.left!=None:
                    node_tmp.append(i.left)
                if i.right!=None:
                    node_tmp.append(i.right)
            nodelist_final.append(node_val_tmp)
            node_val_tmp = []
            nodeList=node_tmp
            node_tmp=[]
        return nodelist_final

pRoot=create_tree.fromList([8,6,10,5,7,9,11])
a=Solution()
print(a.Print(pRoot))