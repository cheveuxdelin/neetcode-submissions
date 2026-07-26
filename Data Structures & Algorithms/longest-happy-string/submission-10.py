import typing

class HeapCharacterElement(typing.NamedTuple):
    negative_count: int
    character: str

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [HeapCharacterElement(*x) for x in [(-a, "a"), (-b, "b"), (-c, "c")] if x[0]]
        heapq.heapify(heap)

        result = []
        character_in_cooldown = None

        while heap:
            element = heapq.heappop(heap)
            new_count = element.negative_count + 1
            result.append(element.character)

            if character_in_cooldown:
                heapq.heappush(heap, character_in_cooldown)
                character_in_cooldown = None

            if new_count:
                updated_element = HeapCharacterElement(new_count, element.character)
                if len(result) >= 2 and result[-1] == result[-2]:
                    character_in_cooldown = updated_element
                else:
                    heapq.heappush(heap, updated_element)

        return "".join(result)
            
