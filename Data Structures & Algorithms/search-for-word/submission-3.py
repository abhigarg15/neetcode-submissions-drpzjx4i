class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        
        path = set()

        def dfs(i,j,idx):
            if idx == len(word):
                return True

            if (min(i,j) < 0 or 
                i >= ROWS or 
                j >= COLS or
                board[i][j] != word[idx] or 
                (i,j) in path):
                return False
            
            path.add((i,j))
            res = dfs(i+1,j,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i,j-1,idx+1)

            path.remove((i,j))
            return res
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True

        return False