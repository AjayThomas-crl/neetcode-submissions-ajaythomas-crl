class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        
        def rec(i,s):
            if i>=len(nums) or s>target:
                return 
            if s==target:
                res.append(cur.copy())
                return 
                
            cur.append(nums[i])
            rec(i,s+nums[i])
            cur.pop()
            
            rec(i+1,s)

            
            
        
        rec(0,0)
        return res
        