
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)

        # (time_that_is_available, remaining)
        on_cooldown = collections.deque()
        t = 0

        while max_heap or on_cooldown:
            if not max_heap and on_cooldown:
                t = on_cooldown[0][0]
            else:
                t += 1
            
            while on_cooldown and on_cooldown[0][0] <= t:
                heapq.heappush(max_heap, on_cooldown.popleft()[1])
            
            if max_heap:
                current_popped = heapq.heappop(max_heap)
                if current_popped + 1 != 0:
                    on_cooldown.append((t + n + 1, current_popped + 1))
        return t