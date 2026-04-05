class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # i believe we need to implement topological sort and detect if there are any cycles or not preset
        # we cant implement topological sort since it is not a directed graph, 
        # topological sort can only happen when we have a directed graph not on indirected graph
        
        graph = defaultdict(list)

        if len(edges) > n-1:
            return False #if the number of edges are more than the 

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node,par):
            if node in visited:
                return False

            visited.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                if not dfs(nei,node):
                    return False

            return True

        
        return dfs(0,-1) and len(visited) == n






        