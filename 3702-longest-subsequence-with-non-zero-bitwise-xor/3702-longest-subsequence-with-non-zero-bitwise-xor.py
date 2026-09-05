class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        XOR = 0
        non_zero = False
        for i in nums:
            XOR = XOR^i
            if i!=0:
                non_zero = True

        if XOR!=0:
            return len(nums)

        if non_zero:
            return len(nums)-1

        return 0                

        
       

            
        

        