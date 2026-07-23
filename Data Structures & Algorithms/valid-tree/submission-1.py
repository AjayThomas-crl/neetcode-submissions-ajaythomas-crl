class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pm={i:[] for i in range(n)}
        for a,b in edges:
            pm[a].append(b)
            pm[b].append(a)
        vis=set()
        def dfs(i,prev):
            if i in vis:
                return False
            vis.add(i)

            for p in pm[i]:
                if p==prev:
                    continue
                if not dfs(p,i):
                    return False
                    
            return True

        if not dfs(0,-1):
            return False
        print (vis)
        return len(vis)==n