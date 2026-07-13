class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        res=[]
        if l==r:
            return nums
        tmax=0
        while(l<r and r<len(nums)):
            tmax=0
            for i in range(l,r+1,1):
                tmax=max(tmax,nums[i])
            res.append(tmax)
            l+=1
            r+=1
        return res
