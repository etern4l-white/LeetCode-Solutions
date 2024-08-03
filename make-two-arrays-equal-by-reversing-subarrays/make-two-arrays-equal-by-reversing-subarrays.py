class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = {}
        dd = {}
        for i in target:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        
        for i in arr:
            if i not in dd:
                dd[i] = 1
            else:
                dd[i]+=1
        
        for i in d:
            if i not in dd or d[i] != dd[i]:
                return False
        return True
