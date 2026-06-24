class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.c=0
        self.grid=grid
        self.visited=[[False]*len(self.grid[0]) for _ in range (len(self.grid))]
        
        
        def bfs(i,j):
            q=deque()
            q.append([i,j])
            self.visited[i][j]=True
            self.grid[i][j]="0"
            ex=[[-1,0],[1,0],[0,1],[0,-1]]
            while(q):
                
                t=q.popleft()
                x=t[0]
                y=t[1]
                for ax,ay in ex:
                    if(x+ax<len(self.grid) and y+ay<len(self.grid[0]) and x+ax>=0 and y+ay>=0 and  not self.visited[x+ax][y+ay] and self.grid[x+ax][y+ay]=="1"):
                        self.visited[x+ax][y+ay]=True
                        q.append([x+ax,y+ay])
                        self.grid[x+ax][y+ay]="0"
            
            self.c+=1
        
        for i in range (0,len(self.grid)):
            for j in range(0,len(self.grid[0])):
                if(self.grid[i][j]=="1" and  not self.visited[i][j]):
                    bfs(i,j)
        return self.c



        