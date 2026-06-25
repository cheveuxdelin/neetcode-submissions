
# [a, b] = b is prerequisite of a
# courses are 0-indexed
# if solution: return any valid ordering
# if no solution: returm empty array
# numCourses >= 1
# prerequisited >= 0
# all prerequisites are unique
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1
        
        queue = collections.deque()
        path = []
        
        for i in range(numCourses):
            if indegrees[i] == 0: # we can start over this node
                queue.append(i)

        while queue:
            current = queue.popleft()
            path.append(current)
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        
        return path if len(path) == numCourses else []