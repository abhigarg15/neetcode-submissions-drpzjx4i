class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj] == "1" and (ni,nj) not in visited:
                    dfs(ni,nj)

        
        ans = 0
        n = len(grid)
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    ans+=1
                    print(ans,i,j)

            
        return ans