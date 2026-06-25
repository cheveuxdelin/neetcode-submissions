class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def helper(opening, closing):
            if closing == n:
                result.append("".join(current))
            else:
                if opening < n:
                    current.append("(")
                    helper(opening+1, closing)
                    current.pop()
                if closing < opening:
                    current.append(")")
                    helper(opening, closing+1)
                    current.pop()

        helper(0, 0)
        return result