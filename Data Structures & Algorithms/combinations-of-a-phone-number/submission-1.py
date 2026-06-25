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
        if not digits:
            return result

        def backtrack(i):
            if i == len(digits):
                result.append("".join(current))
            else:
                for option in d[int(digits[i])]:
                    current.append(option)
                    backtrack(i+1)
                    current.pop()
        backtrack(0)
        return result
            