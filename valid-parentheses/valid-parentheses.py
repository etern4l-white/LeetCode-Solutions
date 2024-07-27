class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        l = [s[0]]
        d = {
            ']':'[',
            '}':'{',
            ')':"("
        }
        for i in s[1:]:
            if i == "[" or i == '{' or i == '(':
                l.append(i)
            else:
                if len(l) == 0:
                    return False
                if l[-1] == d[i]:
                    l.pop()
                else:
                    return False
        return len(l) == 0
        
