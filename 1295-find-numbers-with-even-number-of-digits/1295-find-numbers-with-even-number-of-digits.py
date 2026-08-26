class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for i in nums:
            if len(str(i))%2==0:
                even+=1

        return even        
        