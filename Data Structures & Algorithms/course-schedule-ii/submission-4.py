class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        result = []
        queue = []

        for course, prerequisite in prerequisites:
            indegrees[course] += 1
            graph[prerequisite].append(course)
        
        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)
        
        while queue:
            current = queue.pop()
            result.append(current)
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if not indegrees[neighbor]:
                    queue.append(neighbor)
        return result if len(result) == numCourses else []
        