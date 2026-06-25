class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current = -1
        min_length = min(strs, key= lambda x: len(x))

        for i in range(len(min_length)):
            compare_to = strs[0][i]

            flag = True
            for word in strs:
                if word[i] != compare_to:
                    flag = False
                    break
            if flag:
                current = i
            else:
                break
        return strs[0][:current+1] if current != -1 else ""