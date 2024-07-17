class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,l=0,0
        ll = len(nums)
        ind = []
        s = 0
        while i<ll:
            if nums[i] == val:
                s+=1
            i+=1
        c = ll-s
        k = 0
        i = 0
        while k < c:
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
            i+=1
        return c
