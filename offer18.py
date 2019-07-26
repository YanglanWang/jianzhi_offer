import create_tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Mirror(self, root):
        if root:
            tmp_node=root.right
            root.right=root.left
            root.left=tmp_node
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root


a=Solution()
root=create_tree.fromList([8,6,10,5,7,9,11])
b=a.Mirror(root)
print(b)


# class Solution:
#     def Mirror(self, root):
#         # write code herero
#         node_list=[root]
#         for start in node_list:
#             while start!=None:
#                 tmp=start.left
#                 start.left=start.right
#                 start.right=tmp
#
#                 node_list.extend([start.left,start.right])
#                 break
#         return root