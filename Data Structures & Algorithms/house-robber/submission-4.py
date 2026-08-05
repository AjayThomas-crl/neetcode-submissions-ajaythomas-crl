class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        m={}
        def dfs(i):
            if i in m:
                return m[i]
            if i>=n:
                return 0
            
            take=nums[i]+dfs(i+2)
            nottake=dfs(i+1)
            m[i]=max(take,nottake)
            return m[i]
        return dfs(0)