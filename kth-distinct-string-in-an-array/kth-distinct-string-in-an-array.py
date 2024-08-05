class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        dd = [i for i in d.items() if i[1] == 1]
        if len(dd) >=k:
            return dd[k-1][0]
        else:
            return ""
