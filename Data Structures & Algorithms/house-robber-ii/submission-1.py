class Solution:
    def rob(self, nums: List[int]) -> int:
        
        m={}
        def rec(i,vis):
            if i in m:
                return m[(i,vis)]
            if i>=len(nums) or (vis and i==len(nums)-1) :
                return 0
            if i==0 :
                
                take=nums[i]+rec(i+2,True)
                
                nottake=rec(i+1,False)

            else:
                take=nums[i]+rec(i+2,vis)
                nottake=rec(i+1,vis)

            
            
            m[(i,vis)]=max(take,nottake)

            return max(take,nottake)
        
        return rec(0,False)