class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        ans = []
        n = len(nums)
        for i in range(0,n-1,2):
            ans+=[nums[i+1]]*nums[i]


        return ans    


        