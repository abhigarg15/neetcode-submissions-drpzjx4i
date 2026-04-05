class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(set)
        indegree = {course:0 for course in range(numCourses)}
        for u,v in prerequisites:
            graph[v].add(u)
            indegree[u]+=1

        q = deque([node for node,value in indegree.items() if value == 0])
        nodeVisited = []
        while q:
            course = q.popleft()
            nodeVisited.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(nodeVisited) != numCourses:
            return []
        return nodeVisited
