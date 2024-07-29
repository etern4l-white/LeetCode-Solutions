class Solution:
    def factorize(self, number):
        fs = []
        for i in range(1, int(number**0.5) + 1):
            if number%i==0:
                fs.append(i)
                if number//i != i:fs.append(number//i)
        return fs
    def kthFactor(self, n: int, k: int) -> int:
        fs = sorted(self.factorize(n))
        try:
            return fs[k-1]
        except Exception as e:
            return -1
