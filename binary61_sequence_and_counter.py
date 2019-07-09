# -*- coding:utf-8 -*-
import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    flag=-1
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

    i=-1
    def Deserialize(self, s):
        # write code here
        self.i+=1
        if self.i<len(s):
            if s[self.i]!='$':
                root=TreeNode(int(s[self.i]))
                root.left=self.Deserialize(s)
                root.right=self.Deserialize(s)
            else:
                return None

        return root

    #
    # def createTree(self,nodelist):
    #     if len(nodelist)==1 and nodelist[0]==None:
    #         return None
    #     nodelist[0].right=self.createTree(nodelist[1:])
    #     nodelist[0].left=self.createTree(nodelist[1:])
    #     return nodelist[0]

    # def Deserialize(self, s):
    #     self.flag += 1
    #     # l = s.split(',')
    #     l=s
    #     if (self.flag >= len(s)):
    #         return None
    #     root = None
    #     if (l[self.flag] != '$'):
    #         root = TreeNode(int(l[self.flag]))
    #         root.left = self.Deserialize(s)
    #         root.right = self.Deserialize(s)
    #     return root


root=create_tree.fromList([8,6,10,5,7,9,11])
a=Solution()
s=a.Serialize(root)
result=a.Deserialize(s)
print(result)