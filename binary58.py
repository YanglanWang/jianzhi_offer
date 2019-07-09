import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        list_origin = []
        list_change = []
        list_origin = self.first_visit(pRoot, list_origin)
        list_change = self.last_visit(pRoot, list_change)
        if list_origin == list_change:
            return True
        else:
            return False

    def first_visit(self, pRoot, list_Node):
        if pRoot!=None:
            list_Node.append(pRoot.val)
        else:
            list_Node.append(None)
        if pRoot != None:
            self.first_visit(pRoot.left, list_Node)
            self.first_visit(pRoot.right, list_Node)
        return list_Node

    def last_visit(self, pRoot, list_Node):
        if pRoot!=None:
            list_Node.append(pRoot.val)
        else:
            list_Node.append(None)
        if pRoot != None:
            self.last_visit(pRoot.right, list_Node)
            self.last_visit(pRoot.left, list_Node)
        return list_Node

a=Solution()
# ll=[1,2,3]
# ll.reverse()
pRoot=create_tree.fromList([8,6,6,5,7,7,5])
print(a.isSymmetrical(pRoot))