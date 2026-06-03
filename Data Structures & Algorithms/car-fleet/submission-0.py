class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        c=position
        while(not max(c)>=target):
            for i in range (len(speed)):
                c[i]+=speed[i]

        return len(set(c))
        