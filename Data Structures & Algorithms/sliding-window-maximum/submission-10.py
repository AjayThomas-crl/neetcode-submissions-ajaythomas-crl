class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        h=deque()

        for i in range(l,r+1):
            while h and nums[h[0]]<nums[i]:
                print(h.popleft())
            h.append(i)
        print(h)
        res=[]
        while r<len(nums):
            res.append(nums[h[0]])

            l+=1
            r+=1

            while h and h[0]<l:
                h.popleft()
            while r<len(nums) and h and nums[h[0]]<nums[r]:
                h.popleft()
            h.append(r)
        
        return res