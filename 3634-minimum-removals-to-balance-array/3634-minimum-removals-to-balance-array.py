class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_len = 1
        l,r = 0,0
        while r<len(nums):
            max_ele = nums[r]
            min_ele = nums[l]

            if max_ele>k*min_ele:
                l+=1

            max_len = max(max_len,r-l+1)

            r+=1


        return len(nums)-max_len