class Solution:
    def valid(self, r):
        d = {}
        for i in r:
            if i in d:
                return False
            else:
                d[i] = 1
        return True
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l, r = 0, 1
        d = {}
        d[s[0]] = 1
        siz = 0

        while r <= len(s):
            if self.valid(s[l:r]):
                r+=1
                siz+=1
            else:
                l+=1
                r+=1
        return siz
