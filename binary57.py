import create_tree
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        pFirst=pNode.right
        if pFirst==None:
            if pNode==pNode.next.left:
                return pNode.next
            if pNode==pNode.next.right:
                return pNode.next.next
        while pFirst.left!=None:
            pFirst=pFirst.left
        return pFirst

a=create_tree.fromList([8,6,10,5,7,9,11])
b=Solution()
b.GetNext(a)


