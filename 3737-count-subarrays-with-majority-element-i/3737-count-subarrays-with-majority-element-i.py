class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    count+=1

                if count*2>(j-i+1):
                    ans+=1


        return ans        




        