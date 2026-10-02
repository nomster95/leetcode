# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        curr = head
        nxt = None
        prev = None
        while(curr!=None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev   
        
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = self.reverseList(head)
        t1 = newhead
        t2 = newhead
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while t1!=None or t2!=None:
            sums = carry
            if t1:
                sums = sums + t1.val
            if t2:
                sums = sums + t2.val

            newNode = ListNode(sums%10)
            carry = sums//10
            curr.next = newNode
            curr = curr.next

            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next

        if carry:
            newNode = ListNode(carry)
            curr.next = newNode

        fnode = self.reverseList(dummy.next)

        return fnode           




       