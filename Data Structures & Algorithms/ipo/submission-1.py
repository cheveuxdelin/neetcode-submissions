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

        queue = collections.deque(sorted((capital_needed, profit) for profit, capital_needed in zip(profits, capital)))
        
        # preinitialize heap with projects available at start 
        heap = []
        while queue and queue[0][0] <= current_capital:
            heapq.heappush(heap, -queue.popleft()[1])

        # since heap represents the available projects we can do,
        # once its empty, means we cant do no more projects really
        while count < k and heap:
            negative_profit = heapq.heappop(heap)
            current_capital += -negative_profit

            while queue and queue[0][0] <= current_capital:
                heapq.heappush(heap, -queue.popleft()[1])
            count += 1
        return current_capital
            