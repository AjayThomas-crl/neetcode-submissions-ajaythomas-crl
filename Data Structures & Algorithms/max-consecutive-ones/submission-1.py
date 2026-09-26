class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)==1 and nums[0]==1:
            return 1
        c=0
        i=0
        while(i<len(nums)):
            if i-1>-1 and nums[i-1]==0:
                cc=0
                while(i<len(nums) and nums[i]==1):
                    cc+=1
                    i+=1
                c=max(c,cc)
            i+=1
        return c