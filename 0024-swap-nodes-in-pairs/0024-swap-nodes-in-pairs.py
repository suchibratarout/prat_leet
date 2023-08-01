# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out=[]
        while head:
            out.append(head.val)
            head=head.next
        ans=[]
        for i in range(0,len(out),2):
            val=out[i:i+2]
            ans+=val[::-1]
        final=ListNode(0)
        tmp=final
        for i in ans:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return final.next