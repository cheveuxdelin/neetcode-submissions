class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        s_map = {}
        matching = 0
        i = 0
        result = None

        for j, c in enumerate(s):
            # we add the current one
            s_map[c] = s_map.get(c, 0) + 1
            
            # we handle the current character now matching case
            if c in t_map and s_map[c] == t_map[c]:
                matching += 1
            
            # we expanded until its valid. now we de-expand while its valid
            while matching == len(t_map):
                # we update the result, if the current possible result is shorter than the previous, we update
                if not result or j-i < result[1]-result[0]:
                    result = [i, j+1]

                # now we decrement from the left
                # and update matching if needed
                if s[i] in t_map and s_map[s[i]] == t_map[s[i]]:
                    matching -= 1
                s_map[s[i]] -= 1
                i += 1
        return s[result[0]:result[1]] if result else ""