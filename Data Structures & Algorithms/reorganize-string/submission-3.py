class Solution:
    def reorganizeString(self, s: str) -> str:
        c = collections.Counter(s)
        heap = [(-c[k], k) for k in c]
        result = []

        while heap:
            count, character = heapq.heappop(heap)
            if result and result[-1] == character:
                if not heap:
                    return ""
                else:
                    second_count, second_character = heapq.heappop(heap)
                    result.append(second_character)
                    if second_count+1 < 0:
                        heapq.heappush(heap, (second_count+1, second_character))
                    heapq.heappush(heap, (count, character))
            else:
                result.append(character)
                if count+1 < 0:
                    heapq.heappush(heap, (count+1, character))
        return "".join(result)
