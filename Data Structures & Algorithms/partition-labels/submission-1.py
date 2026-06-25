class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []

        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        
        start = 0
        goal = last_index[s[0]]
        for i, c in enumerate(s):
            goal = max(goal, last_index[c])
            if i == goal:
                result.append(goal-start+1)
                start = goal+1
        return result