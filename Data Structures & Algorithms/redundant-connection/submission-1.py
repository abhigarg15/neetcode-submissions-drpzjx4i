class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n = len(edges)
        # graph = defaultdict(list)
        # indegree = {i:0 for i in range(1,n+1)}
        # for u,v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        #     indegree[u]+=1
        #     indegree[v]+=1

        # print(indegree)
        # q = deque(node for node in range(1,n+1) if indegree[node] == 1)
        # print(q)
        # while q:
        #     node = q.popleft()
        #     indegree[node] -= 1

        #     for nei in graph[node]:
        #         print(f"{node}->{nei}")
        #         indegree[nei]-=1
        #         if indegree[nei] == 1:
        #             q.append(nei)
        
        # print(indegree)
        # for u,v in reversed(edges):
        #     if indegree[u] == 2 and indegree[v]:
        #         return [u,v]

        # return []

        # def hasCycle(curr,parent):
                
        #     print()

        #     print(curr, parent)
        #     if curr in visited:
        #         return True
        #     visited.add(curr)
        #     print(graph[curr])
        #     for nei in graph[curr]:
        #         print(nei,end=" ")
        #         if nei == parent:
        #             continue
        #         if hasCycle(nei,curr):
        #             return True

        #     return False

        # graph = defaultdict(list)
        # for u,v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        #     visited = set()
        #     print(graph)
        #     if hasCycle(u,-1):
        #         return [u,v]
        #     print(visited)

        # return []
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u]+=1
            indegree[v]+=1

        # I am now only considering the end points with only one node connection

        q = deque([node for node in indegree if indegree[node] == 1])


        while q:
            ele = q.popleft()
            indegree[ele]-=1
            for nei in graph[ele]:
                indegree[nei]-=1
                if indegree[nei] == 1:
                    q.append(nei)

        for u,v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u,v]

        return []


    
