class Solution:
    def climbStairs(self, n: int) -> int:
        
        def rec(i):
            if i==n:
                return 1
            if i>n:
                return 0
            

            return rec(i+1)+rec(i+2)
        
        return rec(0)