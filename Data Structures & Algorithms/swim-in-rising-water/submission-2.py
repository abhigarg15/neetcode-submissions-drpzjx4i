class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # we will apply djikstra algorithm

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        minH = [(grid[0][0],0,0)] # weight, row,col

        while minH:
            cost, i, j = heapq.heappop(minH)
            if (i,j) in visited:
                continue
            
            visited.add((i,j))
            if i == ROWS-1 and j == COLS-1:
                return cost 
            
            for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=ni<ROWS and 0<=nj<COLS and (ni,nj) not in visited:
                    
                    heapq.heappush(minH,(max(cost,grid[ni][nj]),ni,nj))


        return -1