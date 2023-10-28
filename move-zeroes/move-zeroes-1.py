class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = [i for i in nums if i != 0]
        l.extend([i for i in nums if i == 0])
        for i,x in enumerate(l):
            nums[i] = x
