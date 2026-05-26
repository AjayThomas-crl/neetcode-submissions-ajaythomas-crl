class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        levels=set()
        ans=0
        while(l<r):
            if(height[l]<=height[r]):
                if(height[l] in levels):
                    l+=1
                    continue
                
                level=height[l]
                i=l+1
                j=r
                while(i<j):
                    if(height[i]<level and i!=0 and i!=len(height)-1):
                        if(len(levels)>0 and height[i]<max(levels)):
                            ans+=level-max(levels)
                        else:
                            ans+=level-height[i]
                        print (ans)
                    i+=1
                print(str(levels)+str(ans)+"l "+str(l))
                for x in range (0,height[l]+1):
                    levels.add(x)
                l+=1
                
            else:
                if(height[r] in levels):
                    r-=1
                    continue
                
                level=height[r]
                i=l+1
                j=r
                while(i<j):
                    if(height[i]<level and i!=0 and i!=len(height)-1):
                        if(len(levels)>0 and height[i]<max(levels)):
                            ans+=level-max(levels)
                        else:
                            ans+=level-height[i]
                    i+=1
                print(str(ans)+"r"+str(height[r])+" "+str(height[l]))
                for x in range (0,height[r]+1):
                    levels.add(x)
                r-=1
                
        return ans
