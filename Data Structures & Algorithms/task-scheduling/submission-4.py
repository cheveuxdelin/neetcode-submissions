
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)

        # (time_that_is_available, remaining)
        on_cooldown = collections.deque()
        current_t = 0

        while max_heap or on_cooldown:
            current_t += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    on_cooldown.append((cnt, current_t + n))
            if on_cooldown and on_cooldown[0][1] == current_t:
                heapq.heappush(max_heap, on_cooldown.popleft()[0])
        return current_t