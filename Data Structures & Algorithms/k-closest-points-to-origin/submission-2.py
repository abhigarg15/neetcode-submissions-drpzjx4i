class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        track = []
        """
        TC = O(n.log(k)) + O(k)
        """
        # for x,y in points: 
        #     dist = (x**2 + y**2)**0.5
        #     if len(track) < k:
        #         heapq.heappush(track, (-dist,x,y))
        #     else:
        #         heapq.heappushpop(track, (-dist,x,y))
        # output = []
        # for _ in range(k):
        #     dist,x,y = heapq.heappop(track)
        #     output.append([x,y])
        # return output


        # points.sort(key = lambda x : x[0]**2 + x[1]**2)
        # return points[:k]

        track = []
        for x,y in points:
            d = x**2 + y**2
            if len(track) < k:
                heapq.heappush(track, (-d,x,y))
            else:
                heapq.heappushpop(track, (-d,x,y))
        
        output = []

        for _ in range(k):
            d,x,y = heapq.heappop(track)

            output.append([x,y])

        return output
