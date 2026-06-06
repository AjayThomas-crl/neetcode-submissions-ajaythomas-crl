class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        o=float('inf')

        while(l<=r):
            mid=(l+r)//2
            print(mid)
            ho=0
            for i in piles:
                ho+=i//mid if i%mid==0 else i//mid+1
                
            if(ho>h):
                l=mid+1
            else:
                o=min(o,mid)
                r=mid-1
        return o
            