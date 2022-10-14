class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        for i in range(len(nums)):
            if total-nums[i]-2*sum(nums[:i]) == 0:
                return i
        return -1
