class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n_visited = 0
        graph = defaultdict(list)
        n_incoming = [0] * numCourses
        q = deque()

        for c, pr in prerequisites:
            graph[pr].append(c)
            n_incoming[c] += 1
        
        for i in range(numCourses):
            if not n_incoming[i]:
                q.append(i)
        
        while q:
            current = q.popleft()
            n_visited += 1
            for neighbor in graph[current]:
                n_incoming[neighbor] -= 1
                if n_incoming[neighbor] == 0:
                    q.append(neighbor)
        return n_visited == numCourses