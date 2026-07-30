# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1 = list1
        for i in range(a-1):
            curr1 = curr1.next
        posA = curr1
        
        curr1 = list1
        for i in range(b):
            curr1 = curr1.next
        posB = curr1.next
        curr2 = list2
        while curr2.next!=None:
            curr2 = curr2.next
        posA.next = list2    
        curr2.next = posB

        return list1    





        

            

        