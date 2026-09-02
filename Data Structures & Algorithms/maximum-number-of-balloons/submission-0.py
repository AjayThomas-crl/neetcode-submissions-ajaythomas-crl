class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m={}
        for i in text:
            m[i]=m.get(i,0)+1
        
        if 'a' not in m or 'b' not in m or 'l' not in m or m['l']<2 or 'o' not in m or m['o']<2 or 'n' not in m:
            return 0
        return min(m['b'],m['a'],m['l']//2,m['n'],m['o']//2)
        