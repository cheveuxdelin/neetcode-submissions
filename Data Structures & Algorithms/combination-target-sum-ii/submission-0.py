# only positives
# no size k
# target > 0
# size > 0

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def backtrack(i, total):
            if total == target:
                result.append(current[:])
            elif total < target and i < len(candidates):
                next_index = i
                while next_index < len(candidates) and candidates[next_index] == candidates[i]:
                    next_index += 1
                
                # skip current
                backtrack(next_index, total)

                # take current
                current.append(candidates[i])
                backtrack(i+1, total+candidates[i])
                current.pop()

        backtrack(0, 0)
        return result

            