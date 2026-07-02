class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        h=set()
        for x in nums:
            h.add(x)
        count=0
        for i in range(len(nums)):
            if nums[i]-1 not in h:
                t=1
                s=nums[i]
                while s+1 in h:
                    s+=1
                    t+=1
                count=max(count,t)
        
        return count