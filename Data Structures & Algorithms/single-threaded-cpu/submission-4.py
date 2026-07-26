import typing

class TaskInBacklog(typing.NamedTuple):
    index: int
    available_at: int
    duration: int

class AvailableTask(typing.NamedTuple):
    duration: int
    index: int

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []

        tasks_ordered_by_arrival = [TaskInBacklog(i, available_at, duration) for i, (available_at, duration) in enumerate(tasks)]
        tasks_ordered_by_arrival.sort(key=lambda task: task.available_at)
        tasks_backlog = collections.deque(tasks_ordered_by_arrival)

        # (duration, index)
        heap = []
        t = 0

        while tasks_backlog or heap:
            while tasks_backlog and tasks_backlog[0].available_at <= t:
                backlog_task = tasks_backlog.popleft()
                heapq.heappush(heap, AvailableTask(backlog_task.duration, backlog_task.index))
            
            if heap:
                available_task = heapq.heappop(heap)
                result.append(available_task.index)
                t += available_task.duration
            else:
                t = tasks_backlog[0].available_at
        return result