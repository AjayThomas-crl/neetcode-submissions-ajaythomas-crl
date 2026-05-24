class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        a=[0]*len(nums)
        h=set(nums)
        
        for i in range (len(nums)):
            t_len=1
            if(nums[i]-1 in h):
                continue
            while(nums[i]+t_len in h):
                t_len+=1
                
            res=max(res,t_len)
            
        return res

