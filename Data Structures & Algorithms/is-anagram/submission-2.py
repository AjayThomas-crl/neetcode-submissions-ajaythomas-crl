class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        for c in s:
            map[c]=map.get(c,0)+1
        
        for c in t:
            if c in map:
                if (map.get(c)==1):
                    map.pop(c)
                else:
                    map[c]-=1
            else:
                return False
        
        return len(map)==0

            
        
        