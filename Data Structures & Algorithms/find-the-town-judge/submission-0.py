class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a=-1
        m={}
        mt={}
        for x,t in trust:
            m[t]=m.get(t,[])+[x]
            mt[x]=mt.get(x,[])+[t]
        
            
        for x,i in m.items():
            if len(i)==n-1 and x not in mt :
               return x
        return -1
