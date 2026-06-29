class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        def dfs(i,j,wi):
            
            if not word[wi]==board[i][j]:
                return False
            
            if wi==len(word)-1:
                return True 
            

            
            return i+1<n and dfs(i+1,j,wi+1) or i-1>=0 and dfs(i-1,j,wi+1) or j+1<m and dfs(i,j+1,wi+1) or j-1>=0 and dfs(i,j-1,wi+1)
        
        for i in range (n):
            for j in range (m):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        
        return False