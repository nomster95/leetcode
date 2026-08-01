# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,nums):
        #base case
        if len(nums)==0:
            return None 


        #recursive case    
        maximum = max(nums)    
        index = nums.index(maximum)
        
        root = TreeNode(maximum)   
        root.left = self.build(nums[ :index])
        root.right = self.build(nums[index+1: ])

        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums)
        
        
      
        
        
        

        