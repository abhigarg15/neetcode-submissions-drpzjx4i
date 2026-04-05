class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for u,v,t in times:
            graph[u].append((v,t))

        dist = {node : float("inf") for node in range(1,n+1)}

        minHeap = [(0,k)]
        visit = set()
        totalTime = 0

        while minHeap:
            w,u = heapq.heappop(minHeap)
            if u in visit:
                continue
            totalTime = w
            visit.add(u)

            for nei,w2 in graph[u]:
                heapq.heappush(minHeap,(w+w2,nei))

        if len(visit) == n:
            return totalTime
        else:
            return -1

        







        # def dfs(node,time):
        #     if dist[node] < time:
        #         return

        #     dist[node] = time
        #     for nei,t in graph[node]:
        #         dfs(nei,time+t)

        # dfs(k,0) # time to reach node k is 0
        # res = max(dist.values())

        # if res != float("inf"):
        #     return res

        # return -1

