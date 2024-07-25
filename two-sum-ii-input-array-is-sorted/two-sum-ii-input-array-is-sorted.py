class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        s = 0
        while(l<r):
            s = nums[l] + nums[r] 
            if s > target:
                r-=1
            elif s < target:
                l+=1
            elif s == target:
                return [l+1, r+1]
        
