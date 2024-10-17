class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list([int(i) for i in str(num)])
        for i in range(len(s)):
            m = i
            for j in range(len(s) - 1, i, -1):
                if s[j] > s[m]:
                    m = j
            if m != i:
                temp = s[m]
                s[m] = s[i]
                s[i] = temp
                return int(''.join([str(x) for x in s]))
        return num
