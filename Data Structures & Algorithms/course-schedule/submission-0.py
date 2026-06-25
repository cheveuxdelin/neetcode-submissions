class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)
        n_incoming = defaultdict(int)
        q = deque()

        for c, pr in prerequisites:
            graph[pr].append(c)
            n_incoming[c] += 1
        
        for i in range(numCourses):
            if i not in n_incoming:
                q.append(i)
        
        while q:
            current = q.popleft()
            visited.add(current)
            for neighbor in graph[current]:
                n_incoming[neighbor] -= 1
                if n_incoming[neighbor] == 0 and neighbor not in visited:
                    q.append(neighbor)
        return len(visited) == numCourses