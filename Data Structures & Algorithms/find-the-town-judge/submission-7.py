class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n+1)

        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        
        try:
            return score.index(n-1, 1)
        except:
            return -1