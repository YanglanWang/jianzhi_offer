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
        # pFirst=pNode.right
        # if pFirst==None:
        #     if pNode==pNode.next.left:
        #         return pNode.next
        #     if pNode==pNode.next.right:
        #         return pNode.next.next
        # while pFirst.left!=None:
        #     pFirst=pFirst.left
        # return pFirst
        if pNode.right==None:
            if pNode.next==None:
                return pNode.next
            if pNode.next.left==pNode:
                return pNode.next
            if pNode.next.right==pNode:
                pNode=pNode.next
                while pNode.next!=None and pNode!=pNode.next.left:
                    pNode=pNode.next
                return pNode.next
        else:
            pNode=pNode.right
            while pNode.left!=None:
                pNode=pNode.left
            return pNode







a=create_tree.fromList([8,6,10,5,7,9,11])
b=Solution()
b.GetNext(a)


