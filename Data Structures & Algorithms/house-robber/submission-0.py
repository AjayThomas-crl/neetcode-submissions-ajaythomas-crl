class Solution:
    def rob(self, nums: List[int]) -> int:
        res=0
        def rec(i,s):
            if i>=len(nums):
                return s
            
            return rec(i+2,s+nums[i])
        return max(rec(0,0),rec(1,0))