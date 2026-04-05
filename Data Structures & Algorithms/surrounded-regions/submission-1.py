class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i,j):
            if board[i][j] != "O":
                return
            board[i][j] = "T"
            for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=ni<ROWS and 0<=nj<COLS and board[ni][nj] == "O":
                    dfs(ni,nj)
        
        ROWS = len(board)
        COLS = len(board[0])

        for i in range(COLS): # we are checking the first and the last row
            if board[0][i] == "O":
                dfs(0,i)
            if board[ROWS-1][i] == "O":
                dfs(ROWS-1,i)

        for j in range(ROWS):
            if board[j][0] == "O": # checking the first column
                dfs(j,0)
            if board[j][COLS-1] == "O":
                dfs(j,COLS-1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"

                


