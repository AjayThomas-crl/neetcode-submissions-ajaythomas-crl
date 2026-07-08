class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        for i in range (n):
            for j in range (m):
                if grid[i][j]==2:
                    q.append((i,j))
        
        res=-1
        while len(q)>0:
            res+=1
            for i in range (len(q)):
                cur=q.popleft()
                d=[[0,1],[0,-1],[1,0],[-1,0]]
                for x in d:
                    r=x[0]+cur[0]
                    c=x[1]+cur[1]

                    if r<n and r>-1 and c>-1 and c<m and grid[r][c]==1:
                        grid[r][c]=2
                        q.append((r,c))

            
            
        for i in range (n):
            for j in range (m):
                if grid[i][j]==1:
                    return -1

        return max(res,0)

