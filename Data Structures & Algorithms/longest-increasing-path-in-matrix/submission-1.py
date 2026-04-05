class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = 1
            for ni,nj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                if 0<=ni<ROWS and 0<=nj<COLS and matrix[ni][nj] > matrix[i][j]:
                    dp[(i,j)] =  max(dp[(i,j)],1 + dfs(ni,nj))

            return dp[(i,j)]
            

        maxLength = 0
        for i in range(ROWS):
            for j in range(COLS):
                maxLength = max(maxLength, dfs(i,j))

        return maxLength