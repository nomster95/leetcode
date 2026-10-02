# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        t1 = l1
        t2 = l2
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

        return dummy.next            




        