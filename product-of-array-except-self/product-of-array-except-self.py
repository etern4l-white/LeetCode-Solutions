class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        right = [nums[-1]]
        for i in nums[1:]:
            left.append(left[-1]*i)
        for i in nums[:-1][::-1]:
            right.insert(0, right[0]*i)
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(right[1])
            elif i == len(nums)-1:
                result.append(left[-2])
            else:
                result.append(left[i-1]*right[i+1])
        return result
