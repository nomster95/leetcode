# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next.next==None:
            return [-1,-1]
        if head.next==None:
            return [-1,-1]    
        curr = head
        ans = []
        while curr!=None:
            ans.append(curr.val)

            curr = curr.next

        store = []
        for i in range(1,len(ans)-1):
            if ans[i]>ans[i-1] and ans[i]>ans[i+1]:
                store.append(i)
            elif ans[i]<ans[i-1] and ans[i]<ans[i+1]:
                store.append(i)

        if len(store)<2:
            return [-1,-1]

        maxDistance = store[-1] - store[0]
        minDistance = maxDistance
        for i in range(len(store)-1):
            dist = abs(store[i]-store[i+1])
            if dist<minDistance:
                minDistance = dist

        return [minDistance,maxDistance]        
               

            






        
        