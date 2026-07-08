class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        for i in range (n):
            for j in range (m):
                if grid[i][j]==2:
                    q.append((i,j))
        
        res=0
        while len(q)>0:
            
            
            res+=1
            for i in range (len(q)):
                cur=q.popleft()
                grid[cur[0]][cur[1]]=2
                if cur[0]+1 < n  and grid[cur[0]+1][cur[1]]==1: q.append((cur[0]+1,cur[1])) 
                if cur[1]+1 < n and grid[cur[0]][cur[1]+1]==1: q.append((cur[0],cur[1]+1)) 
                if cur[0]-1 >= 0 and grid[cur[0]-1][cur[1]]==1: q.append((cur[0]-1,cur[1])) 
                if cur[1]-1 >= 0 and grid[cur[0]][cur[1]-1]==1: q.append((cur[0],cur[1]-1)) 
            print(q)
            
        for i in range (n):
            for j in range (m):
                if grid[i][j]==1:
                    return -1

        return res-1

