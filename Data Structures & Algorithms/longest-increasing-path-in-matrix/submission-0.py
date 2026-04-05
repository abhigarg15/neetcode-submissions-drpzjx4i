class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(i,j,visited):
            if (i,j) in visited:
                return 0

            visited.add((i,j))
            ans = 1
            for ni,nj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                if 0<=ni<ROWS and 0<=nj<COLS and matrix[ni][nj] > matrix[i][j]:
                    ans = max(ans, 1 + dfs(ni,nj,visited))
            visited.remove((i,j))
            return ans 
            

        maxLength = 0
        for i in range(ROWS):
            for j in range(COLS):
                maxLength = max(maxLength, dfs(i,j,set()))

        return maxLength