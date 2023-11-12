# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:return 
        res = [ListNode(head.val, next=None)]
        while head.next != None:
            head = head.next
            res.insert(0, ListNode(val=head.val, next=res[0]))
        return res[0]
        
