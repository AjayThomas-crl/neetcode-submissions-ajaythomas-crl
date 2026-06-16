# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recinvtree(self,root):
        if (root is None):
            return
        
        if(root.left):
            t=root.left
            root.left=root.right
            root.right=t
            

        else:
            t=root.right
            root.right=root.left
            root.left=t
        self.recinvtree(root.left)
        self.recinvtree(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res=root
        self.recinvtree(root)
        return res
            
        