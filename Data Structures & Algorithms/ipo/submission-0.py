# every time finish a project, you will have more capital (if not, ditch the project bc wtf)
# now, after every project finished, you need to re-evaulate which is the one that gives you more
# you need to re-evaluate afer every project finished since you could have budget for a higher yielding project now
# this could be either by sorting each time or keeping a priority queue
# a priority queue will beat sorting each time for complexity
# capital only increases, minimum_capital needed does not substract

# again i believe that we need to separate concerns with two data structures
# the heap will represent excusively the projects that are available right NOW
# and we can have a queue of projects sorted by capital_needed
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        count = 0
        current_capital = w

        available_at_start = []
        not_available_at_start = []

        for profit, capital_needed in zip(profits, capital):
            if capital_needed <= current_capital:
                available_at_start.append(-profit)
            else:
                not_available_at_start.append((capital_needed, profit))

        # (-profit)
        # we need to prepuplate the heap with the available projects right now
        # means we need to group by, avialable_at_start, and not
        heap = available_at_start
        heapq.heapify(available_at_start)
        not_available_at_start.sort()
        
        queue = collections.deque(not_available_at_start)

        # since heap represents the available projects we can do,
        # once its empty, means we cant do no more projects really
        while count < k and heap:
            negative_profit = heapq.heappop(heap)
            current_capital += -negative_profit

            while queue and queue[0][0] <= current_capital:
                heapq.heappush(heap, -queue.popleft()[1])
            count += 1
        return current_capital
            