class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        a=[0]*len(nums)
        
        
        for i in range (len(nums)):
            t_len=1
            
            while(nums[i]+t_len in nums):
                t_len+=1
            res=max(res,t_len)
        return res

