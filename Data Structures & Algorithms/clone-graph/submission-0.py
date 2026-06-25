"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m={}
        if node is None:
            return None
        def dfs(node):
            
            if node in m:
                return m[node]
            
            c=Node(node.val)
            m[node]=c
            for n in node.neighbors:
                if(n in m):
                    c.neighbors.append(m[n])
                else:
                    c.neighbors.append(dfs(n))
            
            
            return c
        
        return dfs(node)
        
        

        

            
            