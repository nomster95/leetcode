class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        case1 = nums[n-1]-nums[2]
        case2 = nums[n-2]-nums[1]
        case3 = nums[n-3]-nums[0]
        return min(case1,case2,case3)
        

        
        