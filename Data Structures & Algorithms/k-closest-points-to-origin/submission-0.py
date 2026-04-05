class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        track = []
        
        for x,y in points:
            dist = (x**2 + y**2)**0.5
            if len(track) < k:
                heapq.heappush(track, (-dist,x,y))
            else:
                heapq.heappushpop(track, (-dist,x,y))
        output = []
        for _ in range(k):
            dist,x,y = heapq.heappop(track)
            output.append([x,y])
        return output