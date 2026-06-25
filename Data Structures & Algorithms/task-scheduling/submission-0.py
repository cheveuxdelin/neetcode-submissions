class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        heap = [-value for value in c.values()]
        heapq.heapify(heap)
        # (ready_time, remaining_count)
        cooldown = collections.deque()

        time = 0
        while heap or cooldown:
            time += 1

            if heap:
                new_count = heapq.heappop(heap) + 1
                if new_count != 0:
                    cooldown.append((time + n, new_count))
            
            while cooldown and cooldown[0][0] <= time:
                heapq.heappush(heap, cooldown.popleft()[1])

        return time