# its just about finding the right permutation
# (if it exists)
# i can see how a heap can give us the right ordering by
# 1. prioritizing the character with the highest count. it will give more space for other characters to be in between.
# 2. prioitizing characters that are availalbe
# :3
# ... theres no idle time or anything, so we just really gotta go by a single ordering criteria, the number of caracters it has
# not true. if it looks like this: ((a, 6), (b, 5))
# yes we pop a, but in next iteration it becomes ((a, 5), (b, 5))
# and we could get a again. there needs to be a tiebreaker
# i think we can just use the index of when it was last used

# this didnt work
# better approach is
# (index_that_we_are_ready_to_use_the_character, -count)
# simplifies the logic
# we just gotta add 2 to current_index

# again, we need a deque to separate between readily available and backlog
# this will solve it as a last approach
# because the heap should represent only the picking between the curently available
# and the deque the ones that are waiting to be available
# why? idk. gemini reply to this please


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        # (-count, character)
        heap = []
        # (index_to_be_available, -count, character)
        backlog = collections.deque()

        result = []

        for character, count in counter.items():
            heapq.heappush(heap, (-count, character))
        
        while heap or backlog:
            current_index = len(result)
            if backlog and backlog[0][0] <= current_index:
                _, negative_count, character = backlog.popleft()
                heapq.heappush(heap, (negative_count, character))
            
            if not heap:
                return ""

            negative_count, character = heapq.heappop(heap)
            
            result.append(character)
            if negative_count < -1:
                backlog.append((current_index+2, negative_count+1, character))
        return "".join(result)
