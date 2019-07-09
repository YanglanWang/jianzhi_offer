class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None


# def reConstructBinaryTree( pre, tin):
#     # write code here
#     if len(pre) == 0:
#         return None
#     root = TreeNode(pre[0])
#     i = tin.index(root.val)
#     root.left = reConstructBinaryTree(pre[1:1 + i], tin[:i])
#     root.right = reConstructBinaryTree(pre[1 + i:], tin[1 + i:])
#     return root

def fromList(sequence):
    treelist=[]
    for i in sequence:
        if i!=None:
            tree_tmp=TreeNode(i)
        else:
            tree_tmp=None
        treelist.append(tree_tmp)
    for i in range(len(treelist)):
        if treelist[i]!=None:
            if 2*i+1<len(treelist):
                treelist[i].left=treelist[2*i+1]
            else:
                treelist[i].left =None
            if 2*i+2<len(treelist):
                treelist[i].right=treelist[2*i+2]
            else:
                treelist[i].right=None
    return treelist[0]
