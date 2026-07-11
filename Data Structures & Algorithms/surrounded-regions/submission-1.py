class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n=len(board)
        m=len(board[0])
        vis=set()
        def rec(i,j):
            if i>=n or i<0 or j>=m or j<0:
                
                return False
            if board[i][j]=="X":
                return True
            if (i,j) in vis:
                return True
            vis.add((i,j))
            dx=[[1,0],[-1,0],[0,1],[0,-1]]
            res=True
            for r,c in dx:
                x=i+r
                y=j+c
                res=res and rec(x,y)
                
            if res :
                board[i][j]="X"
            return res
            
        
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    rec(i,j)
        