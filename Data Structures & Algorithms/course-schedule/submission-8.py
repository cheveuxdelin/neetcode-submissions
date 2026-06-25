class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = defaultdict(int)

        for course, prerequisite in prerequisites:
            indegrees[course] += 1
            graph[prerequisite].append(course)
        
        queue = deque()
        visited = set()

        for i in range(numCourses):
            if i not in indegrees:
                queue.append(i)

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                for neighbor in graph[current]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)
        return len(visited) == numCourses
        

