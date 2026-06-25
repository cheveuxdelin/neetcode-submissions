class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        current = []


        def helper(i, s):
            if s == target:
                result.append(current.copy())
            elif i < len(candidates) and s < target:
                next_index = i
                while next_index < len(candidates) and candidates[next_index] == candidates[i]:
                    next_index += 1
                # skip
                helper(next_index, s)
                # take
                current.append(candidates[i])
                helper(i+1, s+candidates[i])
                current.pop()

        helper(0, 0)
        return result