class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # def bfs(i,j):
        #     q = deque([(i,j,0)])
        #     visited = set()

        #     while q:
        #         i,j,s = q.popleft()

        #         if (i,j) in visited:
        #             continue
        #         visited.add((i,j))

        #         for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
        #             if 0<=ni<ROWS and 0<=nj<COLS and ((ni,nj) not in visited) and grid[ni][nj] != 0 and grid[ni][nj] != -1:
        #                 if grid[ni][nj] > s+1:
        #                     grid[ni][nj] = s+1
        #                 q.append((ni,nj,s+1))
        
        
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j,0))

        while q:
            i,j,s = q.popleft()
            for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=ni<ROWS and 0<=nj<COLS and grid[ni][nj] == 2**31-1:
                    grid[ni][nj] = s+1
                    q.append((ni,nj,s+1))





