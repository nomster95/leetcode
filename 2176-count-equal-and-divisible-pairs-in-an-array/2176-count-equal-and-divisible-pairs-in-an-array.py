class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    count+=1

            ans+=count

        return ans            


        