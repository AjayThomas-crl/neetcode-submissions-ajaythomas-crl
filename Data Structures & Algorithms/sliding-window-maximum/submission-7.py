class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        res=[]
        if k==1:
            return nums
        h=deque()
        for i in range(l,r+1,1):
            while h and nums[h[0]]<nums[i]:
                h.popleft()
            h.append(i)
        
        while(r<len(nums)):
            
            res.append(nums[h[0]])
            l+=1
            r+=1
            while h and h[0]<l:
                h.popleft()
            if r<len(nums):
                while h and nums[h[-1]]<nums[r]:
                    h.pop()
                h.append(r)
            
        return res