class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        current = []

        def helper(i: int):
            if i == len(s):
                if len(current) == 4:
                    result.append(".".join(current))
            elif len(current) < 4:
                if s[i] == "0":
                    current.append(s[i])
                    helper(i+1)
                    current.pop()
                else:
                    for j in range(i, min(i+3, len(s))):
                        value = int(s[i:j+1])
                        if value > 255:
                            break
                        current.append(s[i:j+1])
                        helper(j+1)
                        current.pop()
        helper(0)
        return result