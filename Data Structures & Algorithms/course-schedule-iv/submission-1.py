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

        @functools.cache
        def dfs(current: int, target: int) -> bool:
            if current == target:
                return True
            else:
                for course_that_proceeds_current in graph[current]:
                    if dfs(course_that_proceeds_current, target):
                        return True
                return False
        
        for possible_prerequisite, course in queries:
            # it just has no prerequisites
            # we check if theres a path to it, since it does have prerequisites
            result.append(dfs(possible_prerequisite, course))
        return result
