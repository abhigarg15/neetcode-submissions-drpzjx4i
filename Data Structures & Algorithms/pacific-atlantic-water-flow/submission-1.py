class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(i,j,visited):
            if (i,j) in visited:
                return 
            visited.add((i,j))

            for ni,nj in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                if 0<=ni<ROWS and 0<=nj<COLS and heights[ni][nj] >= heights[i][j]:
                    dfs(ni,nj,visited)


        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        for i in range(COLS):
            dfs(0,i,pacific) # going across the pacific shoreline on the top row
            dfs(ROWS-1,i,atlantic) # going across the atlantic shoreline on the bottom row 

        for j in range (ROWS):
            dfs(j,0,pacific)
            dfs(j,COLS-1, atlantic)


        common = pacific & atlantic

        return [[a,b] for a,b in common]