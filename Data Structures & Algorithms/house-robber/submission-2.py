class Solution:
    def rob(self, nums: List[int]) -> int:
        res=0
        m={}
        def rec(i,s):
            if i in m:
                return m[i]+s
            if i>=len(nums):
                return s
            nottake=rec(i+1,s)
            take=rec(i+2,s+nums[i])
            m[i]=max(take,nottake)
            return max(take,nottake)
        return rec(0,0)