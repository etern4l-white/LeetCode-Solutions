class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {i:1 for i in nums1}
        dd = {i:1 for i in nums2}
        i1, i2 = 0,0
        for i in nums1:
            if i in nums2:
                i1+=1
        
        for i in nums2:
            if i in nums1:
                i2+=1
        return [i1,i2]
