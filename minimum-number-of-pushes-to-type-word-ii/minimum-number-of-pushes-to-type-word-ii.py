class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}
        for i in word:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        keypad = {}
        keys_sorted = sorted([i for i in d.items()], key=lambda x:x[1], reverse=True)
        i = 0
        l = len(keys_sorted)
        w = 1
        n1,n2,n3,n4 = 0,0,0,0
        while i < l:
            if n1<8:
                keypad[keys_sorted[i][0]] = 1
                n1+=1
            elif n2<8:
                keypad[keys_sorted[i][0]] = 2
                n2+=1
            elif n3<8:
                keypad[keys_sorted[i][0]] = 3
                n3+=1
            elif n4<8:
                keypad[keys_sorted[i][0]] = 4
                n4+=1
            i+=1
        s = 0
        for i in d.keys():
            s+=d[i]*keypad[i]
        return s
