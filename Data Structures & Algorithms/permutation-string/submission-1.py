class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c_s1 = Counter(s1)
        current = {}
        i = 0
        for j in range(len(s2)):
            current[s2[j]] = current.get(s2[j], 0) + 1
            if j-i+1 > len(s1):
                current[s2[i]] -= 1
                if current[s2[i]] == 0:
                    current.pop(s2[i])
                i += 1
            if c_s1 == current:
                return True
        return False