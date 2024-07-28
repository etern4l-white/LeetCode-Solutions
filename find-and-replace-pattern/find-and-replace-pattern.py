class Solution:
    def get_code(self, string):
        d = {}
        l = []
        x = 0
        for i in string:
            if i not in d:
                d[i] = x
                l.append(x)
                x+=1
            else:
                l.append(d[i])
        return l
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        org_code = self.get_code(pattern)
        valid = []
        for word in words:
            if self.get_code(word) == org_code:
                valid.append(word)
        return valid
