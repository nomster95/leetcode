# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        nxt = None
        prev = None
        slow = head
        fast = head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        while(slow!=None):
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        first = head
        second = prev
        while(second):
            if(first.val!=second.val):
                return False
                #dont compare the linked list compare the values

            first = first.next
            second = second.next

        return True        


        