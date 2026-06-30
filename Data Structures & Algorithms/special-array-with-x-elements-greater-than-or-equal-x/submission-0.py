class Solution:
    def specialArray(self, nums: List[int]) -> int:
        m=0
        for i in range(1,len(nums)+1):
            c=0
            for x in nums:
                if (i<=x):
                    c+=1
                if c>i:
                    break
            
            if (c==i):
                m=max(m,c)
        
        return m if m!=0 else -1
