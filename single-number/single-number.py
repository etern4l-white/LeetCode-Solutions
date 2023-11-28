class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = nums.count(i)
            if d[i] == 1:
                return i
        
