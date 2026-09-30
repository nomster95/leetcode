class Solution:
    def subarray(self,nums,k):
        freq = {}
        l,r,count = 0,0,0
        while r<len(nums):
            if nums[r] not in freq:
                freq[nums[r]] = 1
            else:
                freq[nums[r]]+=1

            while len(freq)>k:
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    del freq[nums[l]]
                l+=1

            count+= r-l+1
            r+=1

        return count            

        

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.subarray(nums,k) - self.subarray(nums,k-1)

        
        