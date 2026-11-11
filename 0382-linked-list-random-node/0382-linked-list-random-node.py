# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode | None):
        self.head = head
        

    def getRandom(self) -> int:
        chosen = None
        count = 0

        curr = self.head
        while curr!=None:
            count+=1

            check = random.randint(1,count)
            if check==1:
                chosen = curr.val

            curr = curr.next    

        return chosen        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()