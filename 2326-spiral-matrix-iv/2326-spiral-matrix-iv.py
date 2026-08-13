# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        
        
        curr = head
        rowstart = 0
        colstart = 0
        rowend = m-1
        colend = n-1
        while curr!=None:
            #rowstart, colstart-colend:
            for i in range(colstart,colend+1):
                if curr is None:
                    break
                

                matrix[rowstart][i] = curr.val
                curr = curr.next
            rowstart+=1

            
            #colend,rowstart-rowend:
            for i in range(rowstart,rowend+1):
                if curr is None:
                    break

                

                matrix[i][colend] = curr.val
                curr = curr.next
                
            colend-=1
            

            #rowend,colend-colstart:
            for i in range(colend,colstart-1,-1):
                if curr is None:
                    break

                if colstart<=colend:


                    matrix[rowend][i] = curr.val
                    curr = curr.next
                

            rowend-=1  
            

            #colstart,rowend-rowstart:
            for i in range(rowend,rowstart-1,-1):
                if curr is None:
                    break

                if rowstart<=rowend:

                    matrix[i][colstart] = curr.val
                    curr = curr.next
                
            colstart+=1

        return matrix       