
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = collections.Counter(s1)
        s2_dict = {}
        i = 0
        
        for j, c in enumerate(s2):
            s2_dict[c] = s2_dict.get(c, 0) + 1
            if j >= len(s1):
                s2_dict[s2[i]] -= 1
                if s2_dict.get(s2[i]) == 0:
                    s2_dict.pop(s2[i])
                i += 1
            if s1_dict == s2_dict:
                return True
        return False
            