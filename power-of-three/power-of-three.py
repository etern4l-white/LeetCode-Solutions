import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        m = 3
        if n >0:
            # Debugging
            # print(math.log10(n)/math.log10(m))
            # print(m**(math.log10(n)/math.log10(m)), m**int(math.log10(n)/math.log10(m)))
            return n!= 0 and (m**(math.log10(n)/math.log10(m)) == m**int(math.log10(n)/math.log10(m)))
        else:
            return False
            # n = -n
            # return m**(math.log10(n)/math.log10(m)) == m**int(math.log10(n)/math.log10(m)) and int(math.log10(n)/math.log10(m))%2==1
