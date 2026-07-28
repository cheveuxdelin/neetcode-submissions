class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1
        
        stack = []
        result = []

        for i in range(numCourses):
            if indegrees[i] == 0:
                stack.append(i)

        while stack:
            current = stack.pop()
            result.append(current)
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if not indegrees[neighbor]:
                    stack.append(neighbor)
        return result if len(result) == numCourses else []