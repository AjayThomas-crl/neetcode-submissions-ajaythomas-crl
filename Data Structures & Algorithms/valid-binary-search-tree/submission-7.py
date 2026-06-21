# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans=True
    def dfs(self,root,rval):
        if not root:
            
            return

        if (root.left and root.right):
            self.ans=  root.left.val<root.val and root.right.val>root.val and root.left.val<rval and root.right.val>rval
            
        elif(root.left):
            self.ans= root.left.val<root.val and root.left.val<rval 
        
        elif(root.right):
            self.ans=  root.right.val>root.val and root.right.val>rval
        
        if self.ans is False:

            return
        
        self.dfs(root.left,rval)
        if self.ans is False:

            return
        self.dfs(root.right,rval)
        if self.ans is False:

            return

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root,root.val)
        return self.ans
        