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
                
                
                
            # if(height[l]<=height[r]):
            #     leftmax=max(leftmax,height[l])
            #     ans+=min(leftmax,rightmax)-height[l]
            #     l+=1
            # else:
            #     rightmax=max(rightmax,height[r])
            #     ans+=min(leftmax,rightmax)-height[r]
            #     r-=1
        return ans
