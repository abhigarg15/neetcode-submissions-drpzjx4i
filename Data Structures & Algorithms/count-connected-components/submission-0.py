class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                ele = q.popleft()
                for nei in graph[ele]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)


        res = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                res+=1

        return res