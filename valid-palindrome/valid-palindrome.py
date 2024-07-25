class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        o0, o9 = 48, 57
        new_s = []
        for i in s:
            o = ord(i)
            if (o >= 97 and o <= 122) or (o >= 65 and o <= 90) or (o >= o0 and o <=o9):
                new_s.append(i.lower())
        l, r = 0, len(new_s)-1
        while(r>l):
            if new_s[r] != new_s[l]:
                return False
            l+=1
            r-=1
        return True
