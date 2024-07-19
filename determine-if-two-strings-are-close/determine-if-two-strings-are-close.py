class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d = {}
        dd = {}
        for i in word1:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        
        for i in word2:
            if i not in dd:
                dd[i] = 1
            else:
                dd[i]+=1
        
        if d == dd:
            return True
        else:
            for i in d:
                if i not in dd:
                    return False
            for i in dd:
                if i not in d:
                    return False
            for i in d:
                if d[i] == dd[i]:
                    d[i] = None
                    dd[i] = None
            dv = [i for i in list(d.values()) if i != None]
            ddv =  [i for i in list(dd.values()) if i != None]
            for x in range(len(dv)):
                for i in range(len(ddv)):
                    if dv[x] == ddv[i]:
                        dv[x] = 0
                        ddv[i] = 0
                        break
            
            return list(set(dv)) == [0]
