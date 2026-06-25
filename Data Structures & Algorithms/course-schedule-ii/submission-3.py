class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        queue = deque()
        result = []

        for course, prerequisite in prerequisites:
            indegrees[course] += 1
            graph[prerequisite].append(course)
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return result if len(result) == numCourses else []