    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_set = set()
        max_length = 0
        
        i = 0
        for j in range(len(s)):
            while s[j] in current_set:
                current_set.discard(s[i])
                i += 1
            current_set.add(s[j])
            max_length = max(max_length, len(current_set))
        return max_length