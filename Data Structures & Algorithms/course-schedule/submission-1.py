class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # graph = defaultdict(list)
        # indegree = {course : 0 for course in range(numCourses)}

        # for u,v in prerequisites:
        #     graph[v].append(u)
        #     indegree[u] += 1

        # q = deque([node for node,val in indegree.items() if val == 0])
        # nodeVisited = 0
        # while q:
        #     node = q.popleft()
        #     nodeVisited +=1

        #     for nei in graph[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)

        
        # return nodeVisited == numCourses


        indegree = {c:0 for c in range(numCourses)}
        graph = defaultdict(list)


        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1


        q = deque(node for node in indegree if indegree[node] == 0)

        visited = set()

        while q:
            c = q.popleft()
            if c in visited:
                continue
            visited.add(c)

            for nei in graph[c]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        
        return len(visited) == numCourses
