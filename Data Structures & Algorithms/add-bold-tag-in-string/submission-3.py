class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False] * len(s)

        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start+len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)
        
        open_tag = "<b>"
        close_tag = "</b>"
        result = []
        
        for i in range(len(s)):
            if bold[i] and (i == 0 or not bold[i-1]):
                result.append(open_tag)
            
            result.append(s[i])

            if bold[i] and (i == len(s)-1 or not bold[i+1]):
                result.append(close_tag)
        return "".join(result)