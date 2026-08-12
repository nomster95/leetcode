# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        ans = []    
        curr = head
        while curr!=None:
            ans.append(curr.val)
            curr = curr.next

        ans[k-1],ans[-k] = ans[-k],ans[k-1]

        curr = head
        for i in range(len(ans)):
            curr.val = ans[i]
            curr = curr.next

        return head    




           
        