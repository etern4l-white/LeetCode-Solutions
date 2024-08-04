class Solution:
    def count_bits(self, n):
        s = 0
        for i in range(32):
            s+=1 if n & (1<<i) else 0
        return s
    def hammingDistance(self, x: int, y: int) -> int:
        return self.count_bits(x^y)
