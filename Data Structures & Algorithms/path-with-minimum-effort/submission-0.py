class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        minH = [(0,0,0)]
        visited = set()
        while minH:
            diff,i,j = heapq.heappop(minH)

            if i == ROWS-1 and j == COLS-1:
                return diff

            if (i,j) in visited:
                continue

            visited.add((i,j))

            for ni,nj in ((i+1,j),(i-1,j),(i,j+1), (i,j-1)):
                if 0<=ni<ROWS and 0<=nj<COLS and (ni,nj) not in visited:
                    newDiff = abs(heights[ni][nj] - heights[i][j])
                    newDiff = max(diff,newDiff)
                    heapq.heappush(minH,(newDiff,ni,nj))

        return 0
