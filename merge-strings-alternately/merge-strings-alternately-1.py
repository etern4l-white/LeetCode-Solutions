class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        step = min(l1, l2)
        s = ""
        i = 0
        while i<step:
            s+=word1[i]
            s+=word2[i]
            i+=1
        if l1<l2:
            s+=word2[i:]
        else:
            s+=word1[i:]
        return s
