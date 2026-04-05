class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))

        """
        Assuming the distance to all the nodes is infinite first
        """

        distanceToNode = {node:float("inf") for node in range(1,n+1)}

        def dfs(node, time):
            if time >= distanceToNode[node]:
                return

            distanceToNode[node] = time

            for nei,w in graph[node]:
                dfs(nei,time+w)

        dfs(k,0)
        res = max(distanceToNode.values())

        return res if res < float("inf") else -1