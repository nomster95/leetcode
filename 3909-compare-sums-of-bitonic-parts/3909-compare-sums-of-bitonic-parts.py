class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        peak = max(nums)
        k = nums.index(peak)
        ascending_sum = sum(nums[0:k+1])
        descending_sum = sum(nums[k:])

        if ascending_sum>descending_sum:
            return 0
        elif ascending_sum<descending_sum:
            return 1
        else:
            return -1
            
                    


        