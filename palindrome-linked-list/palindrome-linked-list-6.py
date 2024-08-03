# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import numpy as np
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(np.uint8(head.val))
            head=head.next
        la = len(arr)
        l, r = 0,la-1
        while l<r:
            if arr[l] != arr[r]:
                return False
            l+=1
            r-=1
        return True
