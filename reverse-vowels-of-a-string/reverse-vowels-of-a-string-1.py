class Solution:
    def reverseVowels(self, s: str) -> str:
        # d = {'a':0, 'o':0, 'u':0, 'i':0, 'e':0 , 'A':0, 'O':0, 'U':0, 'I':0, 'E':0 }
        # ov = [i for i in s if i in d][::-1]
        # c = 0
        # s = [x for x in s]
        # for i, ch in enumerate(s):
        #     if ch in d:
        #         s[i] = ov[c]
        #         c+=1
        # return ''.join(s)
        d = {'a':0, 'o':0, 'u':0, 'i':0, 'e':0 , 'A':0, 'O':0, 'U':0, 'I':0, 'E':0 }
        l, r = 0,len(s)-1
        s = list(s)
        while l<r:
            if s[l] in d:
                while s[r] not in d:
                    r-=1
                if l == r:break
                temp = s[r]
                s[r] = s[l]
                s[l] = temp
                r-=1
            l+=1
        return ''.join(s)
