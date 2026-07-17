
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        hasCycle = False
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if(slow==fast):
                hasCycle = True
                break
        if(not hasCycle):
            return None    
        
        l = 0
        while(slow.next!=fast):
            slow = slow.next
            l +=1
        l+=1
        
        slow = head
        fast = head

        for i in range(l):
            fast = fast.next

        while(slow!=fast):
            slow = slow.next
            fast = fast.next

        return slow        
            