class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        cur=[]
        def rec(i):
            
            if i>=len(nums):
                res.append(cur.copy())
                return 

            cur.append(nums[i])
            rec(i+1)
            cur.pop()

            while(i+1<len(nums) and nums[i]==nums[i+1]):
                i+=1
            
            rec(i+1)
        
        rec(0)
        return res