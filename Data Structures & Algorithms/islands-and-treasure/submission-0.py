class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for _ in range (n)]
        
        q=deque()
        en=[[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(n):
            for j in range (m):
                if(grid[i][j]==0):
                    q.append([i,j])
                    vis[i][j]=True
        
        dist=0
        while(q):
            for i in range(len(q)):
                e=q.popleft()
                i=e[0]
                j=e[1]
                grid[i][j]=dist
                
                for x in en:
                    ax=i+x[0]
                    ay=j+x[1]

                    if(ax>=0 and ax<n and ay>=0 and ay<m and not vis[ax][ay] and not grid[ax][ay]==0 and not  grid[ax][ay]==-1):
                        q.append([ax,ay])
                        vis[ax][ay]=True
            dist+=1
        
        
       
        

                    
            
            