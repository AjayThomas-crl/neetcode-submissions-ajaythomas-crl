class Solution:
    def climbStairs(self, n: int) -> int:
        
        def rec(c,s):
            if s==n:
                return 1
            if c>n or s>n:
                return 0
            
            take=rec(c,s+c)
            notake=rec(c+1,s)
            return take+notake
        
        return rec(1,0)