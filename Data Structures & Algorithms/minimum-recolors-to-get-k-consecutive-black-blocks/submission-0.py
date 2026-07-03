class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        n_blacks = 0
        result = sys.maxsize

        for j in range(len(blocks)):
            n_blacks += blocks[j] == "B"
            if j >= k:
                n_blacks -= blocks[i] == "B"
                i += 1
            if j >= k - 1:
                result = min(result, k - n_blacks)
        return result
