# -*- coding:utf-8 -*-
import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        sequence=[]
        Nodelist = [root]
        for Node in Nodelist:
            while Node != None:
                sequence.append(Node.val)
                Nodelist.extend([Node.left, Node.right])
                break
        return sequence
a=Solution()
root=create_tree.fromList([8,6,10,5,7,9,11])
b=a.PrintFromTopToBottom(root)
print(b)