class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=deque()
        res=[0]*len(temperatures)
        i=0
        while(i<len(temperatures)):
            if(len(stack)==0 or temperatures[i]<=stack[-1][0]):
                stack.append((temperatures[i],i))
                i+=1
                continue
                
            while(len(stack)>0 and temperatures[i]>stack[-1][0]):
                print(i)
                t=stack.pop()[1]
                print(str(t)+" t")
                print(stack)
                res[t]=i-t
            stack.append((temperatures[i],i))
            i+=1
        return res
