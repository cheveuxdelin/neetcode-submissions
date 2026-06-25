
class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for s in strs:
            for c in str(len(s)):
                arr.append(c)
            arr.append(".")
            for c in s:
                arr.append(c)
        return "".join(arr)

    def decode(self, s: str) -> List[str]:
        rtn = []
        i = 0
        while i < len(s):
            next_dot_index = i
            while s[next_dot_index] != ".":
                next_dot_index += 1
            
            number_of_characters_to_read = int(s[i:next_dot_index])
            
            rtn.append(s[next_dot_index+1:next_dot_index+1+number_of_characters_to_read])
            i = next_dot_index+1+number_of_characters_to_read
        return rtn
            
