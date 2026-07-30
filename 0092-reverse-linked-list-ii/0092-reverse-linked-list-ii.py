# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for i in range(left-1):
            curr = curr.next
        before_left = curr
        left_node = curr.next
        
        prev = None
        curr = left_node
        nxt = None

        for i in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        before_left.next = prev
        left_node.next = curr    

        return dummy.next
