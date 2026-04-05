class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # ROWS = len(board)
        # COLS = len(board[0])
        
        # path = set()

        # def dfs(i,j,idx):
        #     if idx == len(word):
        #         return True

        #     if (min(i,j) < 0 or 
        #         i >= ROWS or 
        #         j >= COLS or
        #         board[i][j] != word[idx] or 
        #         (i,j) in path):
        #         return False
            
        #     path.add((i,j))
        #     res = dfs(i+1,j,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i,j-1,idx+1)

        #     path.remove((i,j))
        #     return res
        
        
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if dfs(i,j,0):
        #             return True

        # return False

        """
        Trying this solution again
        """

        # ROWS = len(board)
        # COLS = len(board[0])
        # path = set()

        # def dfs(r,c,idx):
        #     if idx == len(word):
        #         return True
        #     if min(r,c) < 0 or r >= ROWS or c >= COLS or board[r][c] != word[idx] or (r,c) in path:
        #         return False

        #     path.add((r,c))
        #     res = dfs(r+1,c,idx+1) or dfs(r-1,c,idx+1) or dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1)
        #     path.remove((r,c))
        #     return res
            


        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if dfs(i,j,0):
        #             return True
        
        # return False

        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        def dfs(i,j,idx):
            if (i,j) in visited:
                return False
            
            if idx+1 == len(word):
                return True
            
            visited.add((i,j))

            for ni,nj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                if 0<=ni<ROWS and 0<=nj<COLS and board[ni][nj] == word[idx+1]:
                    if dfs(ni,nj,idx+1):
                        return True

            visited.remove((i,j))
            return False




        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True

        return False


        

