class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        d = {}
        for x, i in enumerate(gs):
            if i not in d:
                d[i] = [x]
            else:
                d[i].append(x)
        
        l = []
        for i in d:
            hi = []
            for j in d[i]:
                if len(hi) == i:
                    l.append(hi)
                    hi = [j]
                else:
                    hi.append(j)
            if len(hi) == i:
                l.append(hi)
        return l
