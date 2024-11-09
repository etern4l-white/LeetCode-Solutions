class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        if n == 1:
            return ([[1]])
        elif n == 2:
            return ([[1], [1,1]])
            
        base = [[1], [1,1]]
        for i in range(3, n+1):
            curr_arr = [1 for i in range(i)]
            for j in range(1, i-1):
                curr_arr[j] = base[i-2][j-1] + base[i-2][j]
            base.append(curr_arr)
        return base
