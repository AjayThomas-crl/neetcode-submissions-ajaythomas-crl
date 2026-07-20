class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        l=0
        j=0
        res=[]
        for n in range (len(nums)):
            if not n==0 and nums[n]==nums[n-1]:
                continue
            l=n+1
            r=len(nums)-1
            tar=nums[n]
            while(l<r):
                t=tar+nums[l]+nums[r]
                while not l==n+1 and nums[l]==nums[l-1]:
                    l+=1
                if t==0:
                    res.append([nums[n],nums[l],nums[r]])
                    l+=1
                elif(t<0):
                    l+=1
                else:
                    r-=1            
        
        return res
