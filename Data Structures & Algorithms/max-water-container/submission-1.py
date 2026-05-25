class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        l=0
        r=len(height)-1

        while(l<r):
            t=0
            if( height[l]<=height[r]):
               
                t=height[l]*(r-l)
                print(t,l,r)
                l+=1
            else:
                t=height[r]*(r-l)
                r-=1
            
            res=max(t,res)   
        return res
        