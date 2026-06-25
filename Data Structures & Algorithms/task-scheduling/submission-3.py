class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-value for value in counter.values()]
        heapq.heapify(heap)
        time = 0
        q = deque() # (-count, idle_time)

        while heap or q:
            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append((count, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
            time += 1
        return time
                