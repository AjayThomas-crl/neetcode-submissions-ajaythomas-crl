class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        vis=[[False]*m for _ in range(n)]
        def dfs(i,j,wi,vis):
            if vis[i][j] or not word[wi]==board[i][j]:
                return False
            
            if wi==len(word)-1:
                return True 
            
            vis[i][j]=True
            found = (
                (i+1 < n and dfs(i+1, j, wi+1, vis)) or
                (i-1 >= 0 and dfs(i-1, j, wi+1, vis)) or
                (j+1 < m and dfs(i, j+1, wi+1, vis)) or
                (j-1 >= 0 and dfs(i, j-1, wi+1, vis))
            )
            vis[i][j]=False
            return found
        
        for i in range (n):
            for j in range (m):
                if board[i][j]==word[0]:
                    
                    if dfs(i,j,0,vis):
                        return True
        
        return False