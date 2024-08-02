class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ms = 2**17
        no = nums.count(1)
        i = 1
        l = len(nums)
        j = i+no-1
        onz = nums[:no].count(0)
        if onz == 0:return 0
        ms = onz if onz < ms else ms
        while i<l:
            if i >= l-no:
                fp = nums[i-1]
                j = j%l
                nv = nums[j]
            else:
                fp = nums[i-1]
                nv = nums[j]
            if fp == 0:
                onz-=1
            if nv == 0:
                onz+=1
            ms = onz if onz < ms else ms
            i+=1
            j+=1
        return ms
