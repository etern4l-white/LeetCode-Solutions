class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = {i:1 for i in banned}
        d = {}
        symbols = {i:1 for i in "!?',;."}
        new_str = []
        for i in paragraph.lower():
            if i not in symbols:
                new_str.append(i)
            else:
                new_str.append(' ')
        new_str = ''.join(new_str).split()
        for word in new_str:
            if word not in ban:
                if word not in d:
                    d[word] = 1
                else:
                    d[word]+=1
        m = 0
        word = None
        for k in d.keys():
            if d[k]>m:
                word = k
                m = d[k]
        return word
