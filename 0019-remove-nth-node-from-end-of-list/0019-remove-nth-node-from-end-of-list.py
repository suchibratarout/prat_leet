# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=b=c=ListNode(0,head)
        i=0
        while c.next.next:
            i=i+1
            if i>=n:
                b=b.next
            c=c.next
        b.next=b.next.next
        return a.next
