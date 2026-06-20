# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
        

        
        

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res=[]
        while (len(q)>0):
            t=None
            for i in range (len(q)):
                t=q.popleft()
                if(t.left):
                    q.append(t.left)
                if(t.right):
                    q.append(t.right)
            res.append(t.val)
        return res