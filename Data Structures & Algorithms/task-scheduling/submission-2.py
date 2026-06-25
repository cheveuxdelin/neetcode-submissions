class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-value for value in count.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque() # pairs of [-count, idle_tine]

        while max_heap or q:
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
            time += 1
        return time