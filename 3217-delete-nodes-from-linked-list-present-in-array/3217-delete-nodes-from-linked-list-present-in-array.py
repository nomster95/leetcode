# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        scan = set(nums)
        while head is not None and head.val in scan:

            head = head.next

        curr = head
        
        while curr.next!=None:
            if curr.next.val in scan:
                curr.next = curr.next.next
               
            else:

                curr = curr.next    

        return head        
        