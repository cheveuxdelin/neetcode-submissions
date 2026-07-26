# there are multiple ways to do a happy string given the constraints a, b, c
# since a,b,c represent MAX amount and not the required amount
# its about maximizing these counts used
# the key to maximizing is to try do substrings of two same characters always
# so like aa+rest, always try do pairs
# we will have to have a cooldown for this last third item, because we then will want to choose
# the one that has more remaining letters yet
# but this has to be discerned from whether its available or not
# separation of concerns by two distinct data structures

# we will be able to do this by:
# greeedily, if remaining >= 2:
# take two carachters
# else, take 1
# if we do choose 2,
# we put that character into a cooldown for 1 turn
# the count can be zero

# my implementation was correct
# however this is not solving the problem
# class Solution:
#     def longestDiverseString(self, a: int, b: int, c: int) -> str:
#         heap = [x for x in [(-a, "a"), (-b, "b"), (-c, "c")] if x[0]]
#         heapq.heapify(heap)

#         result = []
#         character_in_cooldown = None

#         while heap:
#             print(heap)
#             remaining_count, character = heapq.heappop(heap)

#             if character_in_cooldown:
#                 heapq.heappush(heap, character_in_cooldown)
#                 character_in_cooldown = None
            
#             if remaining_count <= -2:
#                 result.extend([character, character])
#                 remaining_count += 2
#                 if remaining_count != 0:
#                     character_in_cooldown = (remaining_count, character)
#             else:
#                 result.append(character)
#                 remaining_count += 1
#                 if remaining_count != 0:
#                     heapq.heappush(heap, (remaining_count, character))
#         return "".join(result)

# on a change of perspective,
# theres no reason to not simulate the whole thing
# instead of choosing between picking 1 or 2
# always pick 1
# and whenever we hit 2 of the same character in a row
# put that character into cooldown
# if there is not other option,
# we finish
# if one solution is more general and simple than the other one
# prefer
# always break down a problem to its simplest procedure
# dont overcomplicate a solution
# for example in recursion
# if one base case encloses the other
# you just need to write one basecase
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [x for x in [(-a, "a"), (-b, "b"), (-c, "c")] if x[0]]
        heapq.heapify(heap)

        result = []
        character_in_cooldown = None

        while heap:
            remaining_count, character = heapq.heappop(heap)
            remaining_count += 1
            result.append(character)

            if character_in_cooldown:
                heapq.heappush(heap, character_in_cooldown)
                character_in_cooldown = None

            if remaining_count:
                if len(result) >= 2 and result[-1] == result[-2]:
                    character_in_cooldown = (remaining_count, character)
                else:
                    heapq.heappush(heap, (remaining_count, character))

        return "".join(result)
            
