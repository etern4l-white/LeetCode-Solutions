# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        return b if a == 0 else self.gcd(b%a, a)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        org_head = head
        while head.next:
            i = self.gcd(head.val, head.next.val)
            node = ListNode()
            node.val = i
            node.next = head.next
            head.next = node
            head = head.next.next
        return org_head
