class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        s = 0
        for i in d:
            if d[i] == 2:
                s^=i
        return s
