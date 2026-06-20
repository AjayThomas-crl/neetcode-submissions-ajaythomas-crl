# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()

        res=[]

        q.append(root)
        
        while(len(q)>0):
            t=[]
            
            for i in range(len(q)):
                n=q.popleft()
                t.append(n.val)
                if(n.left):
                    q.append(n.left)
                if(n.right):
                    q.append(n.right)
            res.append(t)
        return res

            
            