class Solution:
    def climbStairs(self, n: int) -> int:
        
        m={}
        def dfs(x):
            if x in m:
                return m[x]
            if x==n:
                return 1
            if x>n :
                return 0
            
            m[x]=dfs(x+1)+dfs(x+2)

            return m[x]
            
        
        
        return dfs(0)
            