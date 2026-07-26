class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []

        # (index, (available_at, duration))
        tasks_ordered_by_arrival = [*enumerate(tasks)]
        tasks_ordered_by_arrival.sort(key=lambda x: x[1][0])
        tasks_backlog = collections.deque(tasks_ordered_by_arrival)

        # (duration, index)
        heap = []
        t = 0

        while tasks_backlog or heap:
            while tasks_backlog and tasks_backlog[0][1][0] <= t:
                index, task = tasks_backlog.popleft()
                heapq.heappush(heap, (task[1], index))
            
            if heap:
                completion_time, index = heapq.heappop(heap)
                result.append(index)
                t += completion_time
            else:
                t += 1
        return result