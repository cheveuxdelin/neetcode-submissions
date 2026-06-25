class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n+1)

        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        
        judge = None
        
        for i in range(1, n+1):
            if score[i] == n-1:
                if not judge:
                    judge = i
                else:
                    return -1
        return judge or -1
        