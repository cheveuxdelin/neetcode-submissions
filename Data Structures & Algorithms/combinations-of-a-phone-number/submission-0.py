class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

        current = []
        result = []

        def backtrack(i):
            if len(current) == len(digits):
                if len(current):
                    result.append("".join(current))
            else:
                for digit in d[int(digits[i])]:
                    current.append(digit)
                    backtrack(i+1)
                    current.pop()
        backtrack(0)
        return result