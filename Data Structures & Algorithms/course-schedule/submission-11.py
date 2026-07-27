# topological sort problem
# its about finding the ones that have no indegrees
# processing them
# and then finding new ones that are available after indegrees-1

# since they can only reach zero indegrees once (they can only decrease)
# no need for visited

# i dont think the order of the queue matters, so it might as well could be a stack
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1
        
        queue = collections.deque()
        n_processed = 0

        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)

        while queue:
            current = queue.popleft()
            n_processed += 1
            for neighbor in graph[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return n_processed == numCourses