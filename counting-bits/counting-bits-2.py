class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for j in range(n+1):
            s = 0
            while j>0:
                s+=j%2
                j//=2
            arr.append(s)
        return arr
