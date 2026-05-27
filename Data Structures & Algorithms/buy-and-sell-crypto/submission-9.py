class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        a=0
        while(r<len(prices)):
            p=prices[r]-prices[l]
            if(l==r):
                r+=1
                continue
            if(p<0):
                l+=1
            elif(p>=0):
                a=max(p,a)
                r+=1

        return a

        