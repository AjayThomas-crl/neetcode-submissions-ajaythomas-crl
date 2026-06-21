# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans=False
    def dfs(self,root):
        if not root:
            return 

        if (root.left and root.right):
            self.ans=  root.left.val<root.val and root.right.val>root.val
            
        elif(root.left):
            self.ans= root.left.val<root.val
        
        elif(root.right):
            self.ans=  root.right.val>root.val
        
        self.dfs(root.left)
        self.dfs(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.ans
        