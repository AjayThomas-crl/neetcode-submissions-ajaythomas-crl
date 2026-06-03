class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        c=position
        while(not max(c)>=target):
            for i in range (len(speed)):
                c[i]+=speed[i]
            for j in range (len(speed)):
                if(j in c[j+1:]):
                    mi=min(speed[j],speed[j+1])
                    speed[j]=mi
                    speed[j+1]=mi
        return len(set(c))
        