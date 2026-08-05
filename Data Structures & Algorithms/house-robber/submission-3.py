class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        def dfs(i):
            if i>=n:
                return 0
            
            take=nums[i]+dfs(i+2)
            nottake=dfs(i+1)

            return max(take,nottake)
        return dfs(0)