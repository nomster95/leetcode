# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        dummy = ListNode(0)
        curr = dummy

        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))

        while heap:
            val,i,node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap,(node.val,i,node)) 

        return dummy.next               
       

            
        