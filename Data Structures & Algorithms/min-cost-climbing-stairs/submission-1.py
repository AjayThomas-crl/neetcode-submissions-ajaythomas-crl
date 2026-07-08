class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def rec(i,cost):

            if i<0:
                return min(cost[0],cost[1])
            
            cost[i]=min(cost[i]+cost[i+1] , cost[i]+cost[i+2] if i+2<len(cost) else cost[i])

            return rec(i-1,cost)

        return rec(len(cost)-2,cost)


        
