class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        s = 0
        i = 0
        while i < 32:
            t = 0
            for num in nums:
                if num&(1<<i) != 0:
                    t+=1
            if t >=k:
                s+=2**i
            i+=1
        return s
