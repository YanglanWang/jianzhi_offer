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
        # # write code here
        # nodelist_final=[]
        # nodeList=[pRoot]
        # node_tmp=[]
        # node_val_tmp=[]
        # while len(nodeList)!=0:
        #     for i in nodeList:
        #         node_val_tmp.append(i.val)
        #         if i.left!=None:
        #             node_tmp.append(i.left)
        #         if i.right!=None:
        #             node_tmp.append(i.right)
        #     nodelist_final.append(node_val_tmp)
        #     node_val_tmp = []
        #     nodeList=node_tmp
        #     node_tmp=[]
        # return nodelist_final


        list_whole=[]
        list_1=[pRoot]
        list_2=[]
        while len(list_1)!=0:
            list_1_int=[r.val for r in list_1 if r!=None]
            list_whole.append(list_1_int)
            for i in list_1:
                # list_whole.append(i)
                list_2=list_2+[i.left]+[i.right]
            list_1=list_2
            list_1=[r for r in list_1 if r!=None]
            list_2=[]
        return list_whole


pRoot=create_tree.fromList([8,6,10,5,7,9,11])
a=Solution()
print(a.Print(pRoot))