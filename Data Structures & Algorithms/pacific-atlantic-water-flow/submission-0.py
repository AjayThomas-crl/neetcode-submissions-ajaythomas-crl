class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n=len(heights)
        m=len(heights[0])
        self.pas=False
        self.atl=False
        def dfs(r,c):
            if r<0 or  r>n or c<0 or c>m:
                return 
            if self.pas and self.atl:
                return
            if r==n-1 and c==0 or r==0 and c==m-1:
                self.pas=True
                self.atl=True
                return
            if r==0 or c==0:
                self.pas=True
            if r==n-1 or c==m-1:
                self.atl=True
                
            en=[[-1,0],[1,0],[0,-1],[0,1]]
            for x in en:
                    ax=r+x[0]
                    ay=c+x[1]
                    if(ax>=0 and ax<n and ay>=0 and ay<m and heights[r][c]>=heights[ax][ay]):
                        dfs(ax,ay)
        res=[]
        for i in range(n):
            for j in range(m):
                self.pas=False 
                self.atl=False
                dfs(i,j)
                if(self.pas and self.atl):
                    res.append([i,j])
        
        return res
                        
                        


