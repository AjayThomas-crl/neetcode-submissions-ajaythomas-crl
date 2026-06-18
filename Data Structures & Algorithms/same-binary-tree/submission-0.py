# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and not q):
            return True
        
        self.ans=True
        def rec(p,q):
            if not p or not q:
                if(not p and q or p and not q):
                    self.ans=False
                return
            
            if(p.val != q.val):
                self.ans=False
            
            rec(p.left,q.left)
            rec (p.right,q.right)
        rec(p,q)
        return self.ans