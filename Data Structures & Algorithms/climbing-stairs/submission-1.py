class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def climb(i):
            if i <= 2:
                return i

            if memo[i] != -1:
                return memo[i]

            memo[i] = climb(i - 1) + climb(i - 2)
            return memo[i]
        
        return climb(n)