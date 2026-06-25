class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s2_map = {}
        i = 0
        matching = 0

        for j, c in enumerate(s2):
            s2_map[c] = s2_map.get(c, 0) + 1

            if j >= len(s1):
                if s2_map[s2[i]] == s1_map[s2[i]]:
                    matching -= 1
                s2_map[s2[i]] -= 1
                i += 1
            

            if s2_map[c] == s1_map[c]:
                matching += 1


            if matching == len(s1_map):
                return True
        return False


