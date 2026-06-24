class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m=0
        self.grid=grid
        
        def bfs(i,j):
            c=0
            q=deque()
            q.append([i,j])
            self.grid[i][j]=0
            ex=[[-1,0],[1,0],[0,1],[0,-1]]
            while(q):
                c+=1
                t=q.popleft()
                x=t[0]
                y=t[1]
                for ax,ay in ex:
                    if(x+ax<len(self.grid) and y+ay<len(self.grid[0]) and x+ax>=0 and y+ay>=0 and self.grid[x+ax][y+ay]==1):
                        q.append([x+ax,y+ay])
                        self.grid[x+ax][y+ay]=0
            
            self.m=max(self.m,c)

        for i in range (0,len(self.grid)):
            for j in range(0,len(self.grid[0])):
                if(self.grid[i][j]==1):
                    bfs(i,j)
        return self.m