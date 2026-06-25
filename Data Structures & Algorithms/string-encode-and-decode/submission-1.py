
class Solution:

    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}.{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
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
            
