class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        indegree = {node : 0 for node in range(1,n+1)}
        graph = defaultdict(list)

        for u,v in trust:
            graph[u].append(v)
            indegree[v]+=1

        for key, val in indegree.items():
            if val == n-1 and len(graph[key]) == 0:
                return key

        return -1
