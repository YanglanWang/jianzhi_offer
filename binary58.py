import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
    #     # write code here
    #     list_origin = []
    #     list_change = []
    #     list_origin = self.first_visit(pRoot, list_origin)
    #     list_change = self.last_visit(pRoot, list_change)
    #     if list_origin == list_change:
    #         return True
    #     else:
    #         return False
    #
    # def first_visit(self, pRoot, list_Node):
    #     if pRoot!=None:
    #         list_Node.append(pRoot.val)
    #     else:
    #         list_Node.append(None)
    #     if pRoot != None:
    #         self.first_visit(pRoot.left, list_Node)
    #         self.first_visit(pRoot.right, list_Node)
    #     return list_Node
    #
    # def last_visit(self, pRoot, list_Node):
    #     if pRoot!=None:
    #         list_Node.append(pRoot.val)
    #     else:
    #         list_Node.append(None)
    #     if pRoot != None:
    #         self.last_visit(pRoot.right, list_Node)
    #         self.last_visit(pRoot.left, list_Node)
    #     return list_Node

#-------method 2:including create duichen shu and bianli original tree and duichen tree.------
        a=self.bianli(pRoot)
        pRoot=self.duichen(pRoot)
        b=self.bianli(pRoot)
        for i in range(len(a)):
            if (a[i] == None and b[i] != None) or (a[i] != None and b[i] == None) or (
                    a[i] != None and b[i] != None and a[i].val != b[i].val):
                return False
        return True
    #
    #
    def duichen(self,pRoot):
        if pRoot==None:
            return None
        if pRoot.left==None and pRoot.right==None:
            return pRoot
        tmp=self.duichen(pRoot.right)
        pRoot.right=self.duichen(pRoot.left)
        pRoot.left=tmp
        return pRoot


    def bianli(self,pHead):
        if pHead == None:
            return [None]

        return [pHead]+self.bianli(pHead.left)+self.bianli(pHead.right)

#---------------end----------------------

#------method1: two bianli and comparision-----------

        if pRoot==None:
            return False
        if (pRoot.left==None and pRoot.right==None):
            return True
        a=self.Pre(pRoot)
        b=self.Pre_duichen(pRoot)
        for i in range(len(a)):
            if (a[i]==None and b[i]!=None) or (a[i]!=None and b[i]==None) or (a[i]!=None and b[i]!=None and a[i].val!=b[i].val):
                return False
        return True

    def Pre(self,pHead):
        if pHead==None:
            return [None]
        return [pHead]+self.Pre(pHead.left)+self.Pre(pHead.right)

    def Pre_duichen(self,pHead):
        if pHead==None:
            return [None]
        return [pHead]+self.Pre_duichen(pHead.right)+self.Pre_duichen(pHead.left)

#--------------------------------------

a=Solution()
# ll=[1,2,3]
# ll.reverse()
# pRoot=create_tree.fromList([1,2,3,4,5,6,7])
pRoot=create_tree.fromList([8,6,6,5,7,7,5])
# pRoot=create_tree.fromList([5,5,5,5,None,None,5,5,None,5])

print(a.isSymmetrical(pRoot))