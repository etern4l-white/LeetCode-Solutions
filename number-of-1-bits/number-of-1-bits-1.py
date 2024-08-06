class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([(n // 2**i)%2 for i in range(32) ])
