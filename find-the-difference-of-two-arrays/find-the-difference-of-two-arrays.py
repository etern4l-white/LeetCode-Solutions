class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]: return [ list(set([i for i in nums1 if not i in nums2])), list(set([i for i in nums2 if not i in nums1])) ]
