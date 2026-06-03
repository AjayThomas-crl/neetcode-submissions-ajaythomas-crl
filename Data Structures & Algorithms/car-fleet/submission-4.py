class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair=[[p,s] for p,s in zip(position,speed)]
        pair.sort(key=lambda x:x[0] ,reverse=True)
        stack=deque()

        for i in pair:
            stack.append(i)
            if(len(stack)>=2):
                s1=stack.pop()
                s2=stack.pop()

                t1=(target-s1[0])/s1[1]
                t2=(target-s2[0])/s2[1]

                if(t1<=t2):
                    stack.append(s2)
                else:
                    stack.append(s2)
                    stack.append(s1)
                
        
        return len(stack)