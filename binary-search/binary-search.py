class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:return 0 
            else: return -1
        
        l, r = 0, len(nums)
        while l < r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m+1
            else:
                r = m
        return -1
