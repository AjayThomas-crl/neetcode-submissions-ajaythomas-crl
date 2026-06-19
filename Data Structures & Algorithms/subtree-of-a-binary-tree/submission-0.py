# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isametree(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if (p.val!=q.val):
            return False
        
        return (self.isametree(p.left, q.left ) and self.isametree(p.right,q.right)) 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(self.isametree(root,subRoot)):
            return True
        
        return (self.isametree(root.left,subRoot) or self.isametree(root.right,subRoot))
        
        

        
