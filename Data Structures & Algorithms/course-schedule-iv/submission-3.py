import functools
# this doesnt seem to be a topological sort,
# but rather, just a dfs search
# building the graph and looking if within the path of prerequirements,
# we find x to be the prerequisite of y
# nothing more

# what about cycles?
# constrainsts say we have no cycles
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]

        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)

        result = []
        reachable = [[False] * numCourses for _ in range(numCourses)]

        def dfs(source: int, current: int):
            reachable[source][current] = True
            for neighbor in graph[current]:
                if not reachable[source][neighbor]:
                    dfs(source, neighbor)
        
        for i in range(numCourses):
            dfs(i, i)
        
        for possible_prerequisite, course in queries:
            result.append(reachable[possible_prerequisite][course])
        return result
