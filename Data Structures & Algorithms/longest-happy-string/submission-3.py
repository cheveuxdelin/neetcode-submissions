class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [element for element in ((-a, "a"), (-b, "b"), (-c, "c")) if element[0] != 0]
        heapq.heapify(heap)
        result = []
        

        while heap:
            count, letter = heapq.heappop(heap)
            possible = len(result) < 2 or len(set([letter, result[-1], result[-2]])) != 1
            if not possible:
                if not heap:
                    break
                else:
                    second_count, second_letter = heapq.heappop(heap)
                    result.append(second_letter)
                    if second_count+1 < 0:
                        heapq.heappush(heap, (second_count+1, second_letter))
                    heapq.heappush(heap, (count, letter))
            else:
                result.append(letter)
                if count+1 < 0:
                    heapq.heappush(heap, (count+1, letter))
        return "".join(result)