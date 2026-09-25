class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        ans = 0
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sums = prefix[j+1] - prefix[i]
                num = str(sums)
                if num[0]==str(x) and num[-1]==str(x):
                    ans+=1

        return ans            




        