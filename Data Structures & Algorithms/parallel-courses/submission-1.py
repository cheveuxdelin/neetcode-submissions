# courses are 1 to n
# relations[i][0] preceeds relations[i][1]

# this just reads as the number of layers of a topological sort tbh
# nothing crazy

# there can be no solution!
# which means, in other words, there can be no topological sort
# we gotta check for that
# easiest way is that we didnt process them all
# count number of processed
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        indegrees = [0] * (n+1)

        for prerequisite, course in relations:
            graph[prerequisite].append(course)
            indegrees[course] += 1
        
        current = []
        n_processed = 0
        n_semesters = 0

        for i in range(1, n+1):
            if not indegrees[i]:
                current.append(i)
        
        while current:
            n_semesters += 1
            n_processed += len(current)
            next_semester = []

            for course in current:
                for neighbor in graph[course]:
                    indegrees[neighbor] -= 1
                    if not indegrees[neighbor]:
                        next_semester.append(neighbor)
            current = next_semester
        return n_semesters if n_processed == n else -1
        
                    