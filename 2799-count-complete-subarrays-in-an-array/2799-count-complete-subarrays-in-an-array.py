class Solution:
    def complete(self,nums,k):
        count = 0
        l,r = 0,0
        if k<=0:
            return 0
        freq = {}
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
                

            
            count+=r-l+1    
            r+=1

        return count    

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        return self.complete(nums,k)-self.complete(nums,k-1)
        
        

        
           