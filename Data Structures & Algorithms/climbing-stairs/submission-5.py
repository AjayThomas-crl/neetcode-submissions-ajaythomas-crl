class Solution:
    def climbStairs(self, n: int) -> int:
        m={}

        def rec(i):
            if i in m:
                return m[i]
            if i==n:
                return 1
            if i>n:
                return 0
            
            x=rec(i+1)+rec(i+2)
            m[i]=x
            return m[i]
        
        return rec(0)