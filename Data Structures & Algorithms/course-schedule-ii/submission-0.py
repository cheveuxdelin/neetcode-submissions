class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            indegrees[course] += 1
            graph[prerequisite].append(course)
        
        path = []
        q = deque()

        for i in range(numCourses):
            if not indegrees[i]:
                q.append(i)
        
        while q:
            current = q.popleft()
            path.append(current)
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if not indegrees[neighbor]:
                    q.append(neighbor)

        return path if len(path) == numCourses else []