class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def dfs(curr,par):
            if curr in visited:
                return False

            visited.add(curr)
            for nei in graph[curr]:
                if nei == par:
                    continue
                if not dfs(nei,curr):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n