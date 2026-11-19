class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        seen = set()
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i]!=target[i] and nums[i] not in seen:
                ans+=1
                seen.add(nums[i])

        return ans        
        