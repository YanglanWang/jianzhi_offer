import create_tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2==None:
            return True
        if pRoot1.val==pRoot2.val:
            result_left=self.IsSubtree(pRoot1.left,pRoot2.left)
            result_right=self.IsSubtree(pRoot1.right,pRoot2.right)
            if result_left==True and result_right==True:
                return True
        else:
            if pRoot1.left!=None:
                result_left=self.HasSubtree(pRoot1.left,pRoot2)
                if result_left==True:
                    return True
                else:
                    if pRoot1.right!=None:
                        result_right=self.HasSubtree(pRoot1.right,pRoot2)
                        if result_right==True:
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                if pRoot1.right != None:
                    result_right = self.HasSubtree(pRoot1.right, pRoot2)
                    if result_right == True:
                        return True
                    else:
                        return False
                else:
                    return False


a=Solution()
pRoot1=create_tree.fromList([8,8,7,9,2,None,None,None,None,4,7])
pRoot2=create_tree.fromList([8,9,2])

print(a.HasSubtree(pRoot1,pRoot2))