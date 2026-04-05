class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = defaultdict(list)
        indegree = { course : 0 for course in range(numCourses)}


        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1

        q = deque([node for node,val in indegree.items() if val == 0])

        visited = set()

        while q:
            node = q.popleft()

            if node in visited:
                continue
            visited.add(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)

        return len(visited) == numCourses