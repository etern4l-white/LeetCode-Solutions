import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:return True
        n = []
        temp = None

        for i in p:
            if i == temp :
                if  i != '*':
                    n.append(i)
            else:
                n.append(i)
                temp = i


        # for i in p:
        #     if i != temp:
        #         n+=i
        #         temp = i
        #     else:
        #         continue

        return s in re.findall(''.join(n), s)
        
