class Solution:
    def findMaxAverage(self, nums: list(), k: int) -> float:
        a = 0-(2**63-1)
        l = len(nums)
        if l <=k:
            return sum(nums)/k
        s = sum(nums[0:k])
        a = s/k
        for i in range(0, l-k):
            s-=nums[i]
            s+=nums[k+i]
            c = s/k
            if c > a:a=c
        return a
