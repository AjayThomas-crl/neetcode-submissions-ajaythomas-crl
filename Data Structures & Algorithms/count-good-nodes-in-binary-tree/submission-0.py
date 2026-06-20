# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []
        q=deque()

        res=[]
        c=1
        q.append(root)
        maxleft=root.val
        maxright=root.val
        
        while(len(q)>0):
            
            
            for i in range(len(q)):
                n=q.popleft()
                
                
                if(n.left):
                    if(n.val<=n.left.val and maxleft<=n.left.val):
                        c+=1
                        res.append(n.left.val)
                    maxleft=max(maxleft,n.val)
                    q.append(n.left)
                if(n.right):
                    if(n.val<=n.right.val and maxright<=n.right.val):

                        c+=1
                        res.append(n.right.val)
                    maxright=max(maxright,n.val)
                    q.append(n.right)
        
        return c
