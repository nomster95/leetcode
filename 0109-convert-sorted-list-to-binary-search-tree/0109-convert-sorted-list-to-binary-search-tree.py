# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        
    def inorder(self,head):
        curr = head
        
        while curr!=None:
            self.ans.append(curr.val)
            curr = curr.next
            

        return head 

    def build(self,left,right):
        if left>right:
            return

        mid = (left+right)//2
        root = TreeNode(self.ans[mid])  

        root.left = self.build(left,mid-1)  
        root.right = self.build(mid+1,right)

        return root

        
       

        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.ans = []
        self.inorder(head)
        return self.build(0,len(self.ans)-1)


        
        
        
        