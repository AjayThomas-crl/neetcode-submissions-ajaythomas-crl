# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self , root,low,high):
        if not root:
            return True
        
        if not (root.val<high and root.val>low):
            return False
        
        return (self.dfs(root.left,low,root.val)and self.dfs(root.right,root.val,high))
        
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.dfs(root,-math.inf,math.inf)
        