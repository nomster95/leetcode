# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = head
        prev = dummy
        sums = 0
        while curr.next!=None:
            if curr.next.val==0:
                Newnode = ListNode(sums)
                prev.next = Newnode
                prev = Newnode
                sums = 0

            sums+=curr.next.val
            curr = curr.next

        return dummy.next    





        