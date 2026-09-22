class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]==nums[j]==nums[k]:
                        good = abs(i-j) + abs(j-k) + abs(k-i)
                        ans.append(good)

        if len(ans)==0:
            return -1                

        return min(ans)                

        