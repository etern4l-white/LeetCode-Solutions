class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result_arr = []
        l1 = len(nums1)
        l2 = len(nums2)
        m = l1+l2
        i, j = 0,0
        while i < l1 and j<l2:
            if nums1[i] <= nums2[j]:
                result_arr.append(nums1[i])
                i+=1
            else:
                result_arr.append(nums2[j])
                j+=1
        if i < l1:
            result_arr.extend(nums1[i:])
        if j < l2:
            result_arr.extend(nums2[j:])
        if m%2==0:
            return (result_arr[m//2-1] + result_arr[m//2])/2
        else:
            return result_arr[m//2]
