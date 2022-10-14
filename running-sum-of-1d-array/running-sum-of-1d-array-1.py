class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = [None]*len(nums)
        a[0] = nums[0]
        for i in range(1, len(nums)):
            a[i] = nums[i] + a[i-1]
        return a
