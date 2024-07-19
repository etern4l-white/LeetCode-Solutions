class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        dd = {}
        for i in ransomNote:
            if i in d:
                d[i]+=1
            else:
                d[i] =1
        for i in magazine:
            if i in dd:
                dd[i]+=1
            else:
                dd[i] =1
        for i in ransomNote:
            if i not in dd:
                return False
            else:
                if dd[i]<d[i]:
                    return False

        return True
        
