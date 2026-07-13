class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        res=[]
        if k==1:
            return nums
        
        h=[]
        
        for i in range(l,r+1,1):
            h.append((-nums[i],i))
        heapq.heapify(h)
        while(r<len(nums)):
        
            while (h and h[0][1]<l):
                heapq.heappop(h)
            res.append(-h[0][0])
            l+=1
            r+=1
            if r<len(nums):
                heapq.heappush(h,(-nums[r],r))
             
        return res
