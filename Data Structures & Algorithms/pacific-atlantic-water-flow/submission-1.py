class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n=len(heights)
        m=len(heights[0])
        
        def dfs(r,c,vis):
            if(vis[r][c]):
                return
            
            vis[r][c]=True
            en=[[-1,0],[1,0],[0,-1],[0,1]]
            for x in en:
                    ax=r+x[0]
                    ay=c+x[1]
                    if(ax>=0 and ax<n and ay>=0 and ay<m and heights[r][c]<=heights[ax][ay]):
                        dfs(ax,ay,vis)
        res=[]
        pac=[[False]*m for _ in range(n)]
        alt=[[False]*m for _ in range(n)]
        for i in range(n):
            dfs(i,0,pac)
        for j in range(m):
            dfs(0,j,pac)

        for i in range(n):
            dfs(i,m-1,alt)
        for j in range (m):
            dfs(n-1,j,alt)

        for i in range(n):
            for j in range(m):
                if pac[i][j]and alt[i][j]:
                    res.append([i,j])
        return res
                        
                        


