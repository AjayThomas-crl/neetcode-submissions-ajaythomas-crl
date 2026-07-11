class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n=len(board)
        m=len(board[0])
        
        def rec(i,j,sur):
            if i>=n or i<0 or j>=m or j<0:
                sur=False
                return
            
            dx=[[1,0],[-1,0],[0,1],[0,-1]]
            for r,c in dx:
                x=i+r
                y=j+c

                if board[x][y]=="O":

                    rec(x,y,sur)
            if sur==True:
                board[i][j]="X"
        
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    rec(i,j,True)
        