# numCourses = number of courses
# courses are 0-indexed
# if solution (finish all courses): return True
# if no solution (cycle): return False
# edge[1] is the prerequisite of edge[0]
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1

        queue = collections.deque()
        count = 0

        for i in range(numCourses):
            if indegrees[i] == 0: # means we can start from here!
                queue.append(i)
        
        
        while queue:
            current = queue.popleft()
            count += 1
            for neighbor in graph[current]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)
        return count == numCourses 
