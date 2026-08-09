class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twoes = 0
        for i in range(len(nums)):
            ones = (ones^nums[i])& ~twoes
            twoes = (twoes^nums[i])& ~ones

        return ones
        