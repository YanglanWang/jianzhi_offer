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
        # nodeList1=[]
        # nodeList2=[]
        # nodeList_final=[]
        # if pRoot==None:
        #     return None
        # if len(pRoot)==0:
        #     return None
        # nodeList1=[pRoot]
        # while len(nodeList1)!=0 or len(nodeList2)!=0:
        #     nodelist_tmp=[]
        #     for i in nodeList1[::-1]:
        #         nodelist_tmp.append(i.val)
        #         nodeList1.remove(i)
        #         if i.left!=None:
        #             nodeList2.append(i.left)
        #         if i.right!=None:
        #             nodeList2.append(i.right)
        #         # nodeList2.extend([i.left,i.right])
        #     nodeList_final.append(nodelist_tmp)
        #
        #     if len(nodeList2)!=0:
        #         nodelist_tmp=[]
        #         for i in nodeList2[::-1]:
        #             nodelist_tmp.append(i.val)
        #             nodeList2.remove(i)
        #             if i.right!=None:
        #                 nodeList1.append(i.right)
        #             if i.left!=None:
        #                 nodeList1.append(i.left)
        #             # nodeList1.extend([i.right,i.left])
        #         nodeList_final.append(nodelist_tmp)
        # return nodeList_final

        list_whole=[]
        list_1=[pRoot]
        list_2=[]
        t=0
        while len(list_1)!=0:
            list_1_int=[r.val for r in list_1 if r!=None]
            list_whole.append(list_1_int)
            for i in list_1:
                # list_whole.append(i)
                if t%2==1:
                    list_2=list_2+[i.right]+[i.left]
                else:
                    list_2=list_2+[i.left]+[i.right]
            list_1=list_2[::-1]
            list_1=[r for r in list_1 if r!=None]
            list_2=[]
            t+=1
        return list_whole



pRoot=create_tree.fromList([1,2,3,4,5,6,7])
a=Solution()
b=a.Print(pRoot)
print(b)