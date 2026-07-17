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

        def helper(i: int):
            if i == len(digits):
                if current:
                    result.append("".join(current))
            else:
                for digit in d[int(digits[i])]:
                    current.append(digit)
                    helper(i+1)
                    current.pop()
        helper(0)
        return result