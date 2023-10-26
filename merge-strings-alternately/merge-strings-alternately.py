class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c1,c2 = 0,0
        l1,l2 = len(word1), len(word2)
        s = ""
        while c1<l1 and c2<l2:
            s+=word1[c1]
            s+=word2[c2]
            c1+=1
            c2+=1
        if c1<l1:
            s+=word1[c1:]
        if c2<l2:
            s+=word2[c2:]
        return s
