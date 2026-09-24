class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ops = -1
        for i in range(len(nums)):
            x = nums[i]
            sums = 0
            
            while x>0:
                digit = x%10
                sums = sums + digit
                x = x//10

            if sums==i:
                ops = i
                break

        return ops      



        