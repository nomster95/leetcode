# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        prev1 = dummy1
        prev2 = dummy2
        curr = head
        
        while curr!=None:
            if curr.val<x:
                prev1.next = curr
                prev1 = curr
                
            else:
                prev2.next = curr
                prev2 = curr

            curr = curr.next 

        prev1.next = dummy2.next
        
            
        prev2.next = None

        return dummy1.next           

