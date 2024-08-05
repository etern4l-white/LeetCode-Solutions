# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ln = []
        left-=1
        right-=1
        while head:
            ln.append(ListNode(val=head.val))
            head = head.next
        new_nl = ln[:left] + ln[left:right+1][::-1] + ln[right+1:]
        i = 0
        while i < len(new_nl)-1:
            new_nl[i].next = new_nl[i+1]
            i+=1
        new_nl[i].next = None
        return new_nl[0]
