class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minima = min(nums)
        maxima = max(nums)
        min_ind = nums.index(minima)
        max_ind = nums.index(maxima)
        min_min = min(max_ind,min_ind)
        max_max = max(max_ind,min_ind)

        op1 = max_max+1
        op2 = len(nums)-min_min
        op3 = (min_min+1) + (len(nums)-max_max)
        return min(op1,op2,op3)

