# Last updated: 7/14/2026, 2:17:08 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, h: Optional[ListNode]) -> Optional[ListNode]:
        if h is None or h.next is None:
            return None
        s=h
        f=h
        p=None
        while f and f.next:
            p=s
            s=s.next
            f=f.next.next
        p.next=s.next
        return h