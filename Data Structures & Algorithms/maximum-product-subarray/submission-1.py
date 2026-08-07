class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma=1
        mi=1
        res=0
        for n in nums:
            if n==0:
                ma,mi=1,1
                continue
            
            tmp=n*ma
            ma=max(n*ma,n*mi,n)
            mi=min(tmp,n*mi,n)
            res=max(ma,res)
        return res
        