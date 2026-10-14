class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            seen = set()
            for j in range(i,len(nums)):
                seen.add(nums[j])
                count+=len(seen)**2



        return count        