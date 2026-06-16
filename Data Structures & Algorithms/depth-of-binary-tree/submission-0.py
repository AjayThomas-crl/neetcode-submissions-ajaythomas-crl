# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def iterate(self,root):
        if(root is None):
            return 0
        
        cl=1+self.iterate(root.left)
        cr=1+self.iterate(root.right)

        return max(cl,cr)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.iterate(root)
            
        