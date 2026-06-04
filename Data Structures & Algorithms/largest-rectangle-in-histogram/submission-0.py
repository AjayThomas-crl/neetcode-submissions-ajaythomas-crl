class Solution:
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        def nextgreat(nums: List[int]):
            stack=deque()
            i=0
            a=[len(nums)]*len(nums)
            while (i<len(nums)):
                while(len(stack)>0 and nums[i]<stack[-1][1]):
                    a[stack.pop()[0]]=i
                    
                stack.append((i,nums[i]))
                i+=1

            return a 
        
        def prevgreat(nums: List[int]):
            stack=deque()
            i=len(nums)-1
            a=[-1]*len(nums)
            while (i>=0):
                while(len(stack)>0 and nums[i]<stack[-1][1]):
                    a[stack.pop()[0]]=i
                    
                stack.append((i,nums[i]))
                i-=1

            return a 
        
        nsc=nextgreat(heights)
        psc=prevgreat(heights)
        print(nsc,psc)
        area=0

        for i in range(len(heights)):
            a=(nsc[i]-psc[i]-1)
            print(a)
            area=max(area,heights[i]*(nsc[i]-psc[i]-1))
        return area
        