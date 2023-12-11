class Solution:
    def is_bit_on(self, i, j):
        return (i & (1<<j)) != 0
    def count_bits(self, i):
        s = 0
        while i > 0:
            i//=2
            s+=1
        return s
    def minFlips(self, a: int, b: int, c: int) -> int:
        ca = self.count_bits(a)
        cb = self.count_bits(b)
        cc = self.count_bits(c)
        longest = max([ca, cb, cc])
        n_of_bits = 0
        for i in range(longest):
            if self.is_bit_on(c, i):
                if (not self.is_bit_on(b, i)) and (not self.is_bit_on(a, i)):
                    n_of_bits+=1
            else:
                if (not self.is_bit_on(b, i)) and (not self.is_bit_on(a, i)):
                    pass
                elif (self.is_bit_on(b, i)) and (self.is_bit_on(a, i)):
                    n_of_bits+=2
                else:
                    n_of_bits+=1
        return n_of_bits
