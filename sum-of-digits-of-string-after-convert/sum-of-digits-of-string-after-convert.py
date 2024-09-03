class Solution:
    def getLucky(self, s: str, k: int) -> int:
        if k == 1:
            return sum([int(x) for x in ''.join([str(ord(i) - 96) for i in s])])
        else:
            ls = ''.join([str(ord(i)- 96) for i in s])
            for i in range(k):
                ss = sum([int(x) for x in ls])
                if i != k-1:
                    ls = str(ss)
            return sum([int(x) for x in ls])
