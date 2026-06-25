class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def generate_key(s: str):
            value = [0] * 26
            for c in s:
                value[ord(c)-ord('a')] += 1
            return tuple(value)
        
        result = defaultdict(list)

        for string in strs:
            key = generate_key(string)
            result[key].append(string)
        
        return list(result.values())
