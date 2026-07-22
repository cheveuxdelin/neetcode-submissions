class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # this seems to be solvable by just making a tree out of every node as root
        # repeated work
        # O(n*E) where n is number of nodes and E is number of edges
        # better solution? idk

        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        best_min_height = sys.maxsize
        result = []

        def calculate_height(root: int) -> int:
            max_height = 0
            visited = set([root])
            stack = [(root, 1)]

            while stack:
                current, current_height = stack.pop()

                # short-circuit
                if current_height > best_min_height:
                    return sys.maxsize
                # update max-height
                max_height = max(max_height, current_height)
                
                for child in graph[current]:
                    if child not in visited:
                        visited.add(child)
                        stack.append((child, current_height + 1))
            return max_height
                    
        for i in range(n):
            candidate_result = calculate_height(i)
            if candidate_result < best_min_height:
                best_min_height = candidate_result
                result = [i]
            elif candidate_result == best_min_height:
                result.append(i)
        return result