class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = []

        for i in range(2**n):
            ss = []
            for j in range(n):
                if (i& (1<<j)) != 0:
                    ss.append(nums[j])
            s.append(ss)
        return s
                
