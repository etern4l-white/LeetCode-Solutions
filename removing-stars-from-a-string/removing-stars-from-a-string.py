class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        c = -1
        for i in s:
            if i == '*':
                res.pop(c)
                c-=1
            else:
                res.append(i)
                c+=1
        return ''.join(res)
        
