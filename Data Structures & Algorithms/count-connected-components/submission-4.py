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
           
            
            vis.add(i)
            
            for p in pm[i]:
                if prev==p:
                    continue
                if p not in vis:
                    dfs(p,i)
            
        
            
        
        for i in range(n):
            if i not in vis:
                dfs(i,-1)
                res+=1
        
        return res