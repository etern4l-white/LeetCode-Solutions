class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j=0,0
        n3 = []
        while True:
            if j == n:
                n3.extend(nums1[i:])
                break
            elif i == m:
                n3.extend(nums2[j:])
                break
            if nums1[i] <= nums2[j]:
                n3.append(nums1[i])
                i+=1
            else:
                n3.append(nums2[j])
                j+=1
            if i>=m and j>=n:
                break
        for i in range(m+n):
            nums1[i] = n3[i]
        
