class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            seen = set()
            curr_sum = 0
            for j in range(i,len(nums)):
                curr_sum+=nums[j]
                seen.add(nums[j])

                if curr_sum in seen:
                    ans+=1


        return ans            


        