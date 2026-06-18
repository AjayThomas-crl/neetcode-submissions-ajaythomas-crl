# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.ans=True
        def height(curr):
            if not curr:
                return 0
            left=height(curr.left)
            right=height(curr.right)

            self.ans=(abs(left-right)<=1)
            

            return 1+max(left,right)
        
        height(root)

        return self.ans