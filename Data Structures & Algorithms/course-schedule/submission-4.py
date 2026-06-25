#cycles allowed?
#we are essentailly detecting cycles i believe

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = defaultdict(int)
        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            indegrees[course] += 1
            graph[prerequisite].append(course)
        
        q = deque()
        processed = 0

        for i in range(numCourses):
            if i not in indegrees:
                q.append(i)
        
        while q:
            current = q.popleft()
            processed += 1
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        return processed == numCourses