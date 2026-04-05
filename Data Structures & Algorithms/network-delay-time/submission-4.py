class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v,t))

        visited = set()
        timeToreach = {}
        def dfs(node,time):
            if node in timeToreach and timeToreach[node] < time:
                return
            timeToreach[node] = time
            for ni,t in graph[node]:
                dfs(ni,time+t)
            
        dfs(k,0)
        if len(timeToreach) != n:
            return -1
        return max(timeToreach.values())