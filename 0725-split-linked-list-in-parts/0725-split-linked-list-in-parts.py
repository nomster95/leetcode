# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        if head is None:
            return [None]*k

        curr = head
        while curr!=None:
            l+=1
            curr = curr.next

        base = l//k
        extra = l%k
        curr = head
        ans = []
        for i in range(k):
            
            part_head = curr
            last = None
            size = base
            if extra>0:
                    size+=1
                    extra-=1
                    
            if size==0:
                ans.append(None)
                continue
      

            for i in range(size):
                last = curr
                curr = curr.next

            last.next = None
            ans.append(part_head)


        return ans   






        
        