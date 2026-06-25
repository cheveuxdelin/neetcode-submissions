class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rtn = []

        def backtrack(left, right, current):
            if len(current) == n * 2:
                rtn.append("".join(current))
            else:
                if left > right:
                    current.append(")")
                    backtrack(left, right+1, current)
                    current.pop()
                if left < n:
                    current.append("(")
                    backtrack(left+1, right, current)
                    current.pop()
        backtrack(0, 0, [])
        return rtn