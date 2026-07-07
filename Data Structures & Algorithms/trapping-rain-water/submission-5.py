class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftmax=height[l]
        rightmax=height[r]
        ans=0

        while(l<r):
            if(leftmax<=rightmax):
                l+=1
                t=min(leftmax,rightmax)-height[l]
                if(t>0):
                    ans+=t
                leftmax=max(leftmax,height[l])
                
                
            else:
                r-=1
                t=min(leftmax,rightmax)-height[r]
                if(t>0):
                    ans+=t
                rightmax=max(rightmax,height[r])
                
                
                
           
        return ans
