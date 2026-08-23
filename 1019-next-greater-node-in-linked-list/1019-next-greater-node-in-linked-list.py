# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        curr = head
        while curr!=None:
            ans.append(curr.val)
            curr = curr.next

        st = []
        n = len(ans)
        nge = [0]*n
        for i in range(n-1,-1,-1):
            while len(st)!=0 and st[-1]<=ans[i]:
                st.pop()

            if len(st)==0:
                nge[i] = 0
            else:
                nge[i] = st[-1]

            st.append(ans[i])

        return nge                    
        