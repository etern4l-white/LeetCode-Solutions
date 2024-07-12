# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_nodes = ListNode()
        rthead = new_nodes
        head = head.next
        cur_sum = 0
        while head != None:
            cur_sum+=head.val
            head = head.next
            if head.val == 0:
                new_nodes.val = cur_sum
                if head.next:
                    new_nodes.next = ListNode(val=0, next=None)
                new_nodes = new_nodes.next
                head = head.next
                cur_sum=0
        return rthead
