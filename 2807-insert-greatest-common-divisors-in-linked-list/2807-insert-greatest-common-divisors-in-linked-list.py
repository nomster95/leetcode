# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self,a:int,b:int):
        while b:
            a,b = b,a%b
        return a
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head

        curr = head  
        
        while curr.next!=None:
            Newnode = ListNode(self.gcd(curr.val,curr.next.val))
            temp = curr.next
            curr.next = Newnode
            Newnode.next = temp
            curr = curr.next.next
        

        return head    

    


        