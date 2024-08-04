class Solution:
    def get_bit(self, number, bit):
        return number & (1<<bit)
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        lls = []
        for i in range(1, n+1):
            j = 0
            while j <= n-i:
                lls.append(sum(nums[j:j+i]))
                j+=1
        sums = sorted(i for i in lls if i != 0)
        return int(sum(sums[left-1:right])%(1e9 + 7))
