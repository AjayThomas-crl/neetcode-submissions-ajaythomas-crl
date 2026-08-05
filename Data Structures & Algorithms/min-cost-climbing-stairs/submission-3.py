class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        m={}
        def dfs(i):
            if i in m:
                return m[i]
            if i>=n:
                return 0
            
            t1=cost[i]+dfs(i+1)
            t2=cost[i]+dfs(i+2)

            return min(t1,t2)
        
        return min(dfs(0),dfs(1))