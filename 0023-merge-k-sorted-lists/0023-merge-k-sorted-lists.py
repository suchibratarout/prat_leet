# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        out=temp=ListNode()
        arr=[]
        for i in lists:
            while i:
                arr.append(i.val)
                i=i.next
        for val in sorted(arr):
            temp.next=ListNode()
            temp=temp.next
            temp.val=val
        return out.next
        