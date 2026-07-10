class Solution:
    def rob(self, nums: List[int]) -> int:
        vis=False
        def rec(i):
            if i>=len(nums):
                return 0
            take=nums[i]+rec(i+2)
            nottake=rec(i+1)

            if i==0 and take>nottake:
                vis=True
                
            return max(take,nottake)
        
        return rec(0)