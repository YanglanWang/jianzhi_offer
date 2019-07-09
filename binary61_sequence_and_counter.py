# -*- coding:utf-8 -*-
import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if root==None:
            return '$'
        left=self.Serialize(root.left)
        right=self.Serialize(root.right)
        result=[str(root.val)]
        result.extend(left)
        result.extend(right)
        return result


    def Deserialize(self, s):
        # write code here
        nodelist=[]
        for i in s:
            if i!='$':
                nodelist.append(TreeNode(int(i)))
            else:
                nodelist.append(None)
        nodestart=nodelist[0]
        nodestart.left=

        for i in range(len(nodelist)):
            # if 2*i+1<len(nodelist):
            if nodelist[i]!=None:
                nodelist[i].left=nodelist[i+1]
            else:
                nodelist[i-1].right=
            # else:
            #     nodelist[i].left=None
            if 2+i+2<len(nodelist):
                nodelist[i].right=nodelist[2*i+2]
            else:
                nodelist[i].left = None
        return nodelist[0]

    def createTree(self,tree):


root=create_tree.fromList([8,6,10,5,7,9,11])
a=Solution()
s=a.Serialize(root)
result=a.Deserialize(s)
print(result)