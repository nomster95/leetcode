class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        even = -1
        for i in nums:
            if i%2==0 and nums.count(i)==1:
                even = i
                break

        return even        
        