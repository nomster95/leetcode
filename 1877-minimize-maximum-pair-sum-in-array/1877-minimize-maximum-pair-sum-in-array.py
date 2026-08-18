class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = []
        i = 0
        j = len(nums)-1
        nums.sort()
        while i<j:
            ans.append(nums[i]+nums[j])
            i+=1
            j-=1

        return max(ans)    

        