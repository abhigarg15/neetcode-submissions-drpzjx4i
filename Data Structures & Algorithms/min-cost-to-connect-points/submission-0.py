class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                manhanttanDist = abs(x1-x2) + abs(y1-y2)
                graph[i].append((manhanttanDist,j))
                graph[j].append((manhanttanDist,i))

        visited = set()
        res = 0
        minH = [(0,0)] # we need to start somewhere

        while len(visited) < n:
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue
            
            visited.add(node)
            res += cost
            for c,nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(minH,(c,nei))

        return res