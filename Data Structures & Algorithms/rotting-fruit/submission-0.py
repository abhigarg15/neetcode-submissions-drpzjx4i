class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j,0))

        maxTime = 0
        while q:
            i,j,t = q.popleft()

            maxTime = max(t,maxTime)

            for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=ni<ROWS and 0<=nj<COLS and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni,nj,t+1))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return maxTime