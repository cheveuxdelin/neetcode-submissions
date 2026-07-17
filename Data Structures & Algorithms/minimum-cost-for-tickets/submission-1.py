class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        queue7 = collections.deque()
        queue30 = collections.deque()

        for day in days:
            while queue7 and queue7[0][0] + 7 <= day:
                queue7.popleft()
            while queue30 and queue30[0][0] + 30 <= day:
                queue30.popleft()
            
            queue7.append((day, cost + costs[1]))
            queue30.append((day, cost + costs[2]))

            cost = min(
                cost + costs[0],
                queue7[0][1],
                queue30[0][1],
            )
        return cost
