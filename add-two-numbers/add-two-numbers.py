# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def ltn(self, l):
        i = 0
        n = 0
        while l:
            n+=l.val*(10**i)
            l = l.next
            i+=1
        return n
    def ntl(self, n):
        i = len(str(n))-1
        # print(n, n&(10**i))
        tail = ListNode(val=(n%(10**(i+1)))//(10**i), next=None)
        i-=1
        while i>=0:
            # print(tail.val)
            node = ListNode(val=(n%(10**(i+1)))//(10**i), next=tail)
            tail = node
            i-=1
        return tail

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = (self.ltn(l1))
        n2 = (self.ltn(l2))
        return self.ntl(n1+n2)
