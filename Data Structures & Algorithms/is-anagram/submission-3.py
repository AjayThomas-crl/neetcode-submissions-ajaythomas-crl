class Solution:
    def isAnagram(self, s: str, t1: str) -> bool:
        
        t2={}
        for t in t1:
            t2[t]=t2.get(t,0)+1
        
        for t in s:
            if t in t2:
                t2[t]=t2.get(t)-1
                if t2[t]==0:
                    t2.pop(t)
            else:
                return False
        print (t2)
        return len(t2)==0

