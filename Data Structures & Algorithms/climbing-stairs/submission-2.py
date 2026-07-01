class Solution:
    def climbStairs(self, n: int) -> int:
        self.c=0
        def dfs(x):
            if x==n:
                self.c+=1
                return
            if x>n:
                return
            
            dfs(x+1)
            dfs(x+2)
        
        dfs(0)
        return self.c
            