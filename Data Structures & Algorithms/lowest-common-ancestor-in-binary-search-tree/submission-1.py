# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def iterate(self,root,p,q):
        if not root or root.val==p.val or  root.val==q.val:
            return root
        if (root.val>p.val and root.val<q.val or root.val<p.val and root.val>q.val):
            return root
        if(p.val>root.val and q.val>root.val):
            return  self.iterate(root.right,p,q)
        else:
            return self.iterate(root.left,p,q)
        # left=self.iterate(root.left,p,q)
        # if(left):
        #     return left
        # else:
        #     return self.iterate(root.right)
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.iterate(root,p,q)