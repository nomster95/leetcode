# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        
        if head.next.next is None:
            head.next = None
            return head

        slow = head
        fast = head.next.next   

        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head        
        