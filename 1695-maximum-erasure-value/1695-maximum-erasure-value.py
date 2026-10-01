class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        l,r = 0,0
        max_sum = 0

        seen = set()
        sums = 0
        while r<len(nums):
            if nums[r] not in seen:
                seen.add(nums[r])
                sums+=nums[r]
                max_sum = max(max_sum,sums)
                r+=1
            else:
                seen.remove(nums[l])
                sums-=nums[l]
                l+=1

        return max_sum            


        