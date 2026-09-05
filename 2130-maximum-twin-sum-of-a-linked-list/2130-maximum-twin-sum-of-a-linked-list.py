# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        nxt = None
        curr = slow
        while curr!=None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first = head
        second = prev
        ans = 0
        while second:
            ans = max(ans,first.val+second.val)
            first = first.next
            second = second.next

        return ans            


        