class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums

        n = len(nums)
        streak = 1
        result = [0]*(n-k+1)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                streak+=1
            else:
                streak = 1

            if i>=k-1:    
                if streak>=k:
                    result[i-k+1] = nums[i]
                else:
                    result[i-k+1] = -1    

        return result        

                

        