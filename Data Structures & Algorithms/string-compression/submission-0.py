class Solution:
    def compress(self, chars: list[str]) -> int:
        index = 0
        current_count = 0
        current_char = chars[0]

        def append_current_char(char: str):
            nonlocal index
            nonlocal current_char
            nonlocal current_count
            chars[index] = current_char
            index += 1
            if current_count > 1:
                for digit in str(current_count):
                    chars[index] = digit
                    index += 1
            current_count = 1
            current_char = char

        for char in chars:
            if char == current_char:
                current_count += 1
            else:
                append_current_char(char)
        append_current_char("")
        return index
