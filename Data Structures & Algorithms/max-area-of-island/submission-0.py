class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(i,j):
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            res = 1
            for ni,nj in ((i+1,j),(i-1,j), (i,j+1), (i,j-1)):
                if 0<=ni<ROWS and 0<=nj<COLS and grid[ni][nj] == 1 and (ni,nj) not in visited:
                    res+=dfs(ni,nj)

            return res

        visited = set()
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)
        
        return maxArea