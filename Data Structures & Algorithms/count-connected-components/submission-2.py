class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pm={}
        for a,b in edges:
            pm[a]=pm.get(a,[])+[b]
            pm[b]=pm.get(b,[])+[a]
        
        vis=set()
        print(pm)
        res=0
        def dfs(i,prev):
            if i in vis:
                return False
            vis.add(i)
            
            for p in pm[i]:
                if prev==p:
                    continue
                if not dfs(p,i):
                    return False
            
        
            return True
        
        for p in pm:
            if dfs(p,-1):
                res+=1
        
        return res