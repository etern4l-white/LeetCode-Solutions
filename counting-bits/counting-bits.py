class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for j in range(n+1):
            s = 0
            for i in range(31, -1, -1):
                s+=1 if j & (1<<i) != 0 else 0
            arr.append(s)
        return arr
    
   
        
