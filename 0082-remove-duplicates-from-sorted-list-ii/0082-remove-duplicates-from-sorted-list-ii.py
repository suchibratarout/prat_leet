# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        dummy = ListNode(-200)
        dummy.next = head
        prev = dummy
        check = 0
        while(head != None and head.next != None):
            if (head.val != head.next.val and check == 0):
                prev = head
                head = head.next
            elif (head.val == head.next.val): 
                if (head.next.next != None):
                    head = head.next
                else:
                    prev.next = None
                    break
                check = 1
            else:
                head = head.next
                prev.next = head
                check = 0
            
        return dummy.next
            
        