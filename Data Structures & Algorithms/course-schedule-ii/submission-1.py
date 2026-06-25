class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            indegrees[course] += 1
            graph[prerequisite].append(course)

        queue = deque()
        result = []

        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)

        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return result if len(result) == numCourses else []
