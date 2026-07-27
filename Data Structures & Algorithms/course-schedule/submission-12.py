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
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        unset = 0
        in_stack = 1
        safe = 2
        state = [unset] * numCourses

        def has_cycle(current: int) -> bool:
            if state[current] == in_stack:
                return True
            if state[current] == safe:
                return False

            state[current] = in_stack

            for neighbor in graph[current]:
                if has_cycle(neighbor):
                    return True
            state[current] = safe
            return False

        for i in range(numCourses):
            if state[i] == unset and has_cycle(i):
                return False
        return True
        
                

                
