class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * (numCourses)
        d = defaultdict(list)

        for a, b in prerequisites:
            d[b].append(a)
            indegrees[a] += 1
        
        queue = collections.deque()

        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            for neighbor in d[current]:
                indegrees[neighbor] -= 1
                if not indegrees[neighbor]:
                    queue.append(neighbor)

        return all(indegree == 0 for indegree in indegrees)