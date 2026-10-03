# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        first = dummy.next
        second = dummy.next.next
        while second!=None:
            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
            first = prev.next
            if first is None:
                break
            second = first.next

            



        return dummy.next       


        