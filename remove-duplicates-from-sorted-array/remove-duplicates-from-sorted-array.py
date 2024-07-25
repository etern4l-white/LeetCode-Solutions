class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        t = 1 if l > 0 else 0
        if l <2:
            return l
        ll = []
        ll.append(nums[0])
        for i in range(1,l):
            if nums[i] != ll[-1]:
                ll.append(nums[i])
                t+=1
        for i in range(t):
            nums[i] = ll[i]
        return t
