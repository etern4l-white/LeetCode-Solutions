class Solution:
    def factorial(self, num):
        if num <= 1:
            return num
        else:
            return num*self.factorial(num-1)
    def trailingZeroes(self, n: int) -> int:
        f = self.factorial(n)
        i = 0
        while(f%10 == 0):
            
            
            f//=10
            if f == 0:
                break
            i+=1
        return i
