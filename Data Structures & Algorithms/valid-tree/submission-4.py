class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        if len(edges) != n-1:
            return False

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node,parent):
            if node in visited:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if dfs(nei,node):
                    return True
            return False


        visited = set()
        for i in range(n):
            if i not in visited:
                if dfs(i,-1):
                    return False
        return True