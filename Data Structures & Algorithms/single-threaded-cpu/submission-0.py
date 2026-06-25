class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enqueue_time = 0
        processing_time = 1
        index = 2
        n = len(tasks)

        result = []
        tasks = [[*task, index] for index, task in enumerate(tasks)]
        tasks.sort(key=lambda x:x[enqueue_time])
        t = 0
        i = 0
        heap = []

        while i < n or heap:
            while i < n and tasks[i][enqueue_time] <= t:
                heapq.heappush(heap, (tasks[i][processing_time], tasks[i][index]))
                i += 1

            if heap:
                task_processing_time, task_index = heapq.heappop(heap)
                t += task_processing_time
                result.append(task_index)
            else:
                t = tasks[i][enqueue_time]
        return result
            
            
            