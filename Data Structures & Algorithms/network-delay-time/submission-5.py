class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # this approach requires a simple dfs and maintaining time to reach every node
        # graph = defaultdict(list)
        # for u,v,t in times:
        #     graph[u].append((v,t))
        
        # timeToreach = {}

        # def dfs(node,time):
        #     if node in timeToreach and timeToreach[node] < time:
        #         return
        #     timeToreach[node] = time
        #     for ni,t in graph[node]:
        #         dfs(ni,time+t)
            
        # dfs(k,0)
        # if len(timeToreach) != n:
        #     return -1
        # return max(timeToreach.values())

        """
        This approach utilizes dijkstra
        """
        graph = defaultdict(list)
        minHeap = [(0,k)]
        maxTime = 0
        visited = set()
        for u,v,t in times:
            graph[u].append((v,t))

        while minHeap:
            time,ele = heapq.heappop(minHeap)
            if ele in visited:
                continue
            maxTime = max(maxTime,time)
            visited.add(ele)
            for u,t in graph[ele]:
                heapq.heappush(minHeap,(time+t,u))

        return maxTime if len(visited) == n else -1