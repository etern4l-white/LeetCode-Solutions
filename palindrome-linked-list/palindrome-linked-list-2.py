# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = [-1 for i in range(100000)]
        i = 0
        while head:
            arr[i] = (head.val)
            head=head.next
            i+=1
        la = i
        l, r = 0,la-1
        while l<r:
            if arr[l] != arr[r]:
                return False
            l+=1
            r-=1
        return True
