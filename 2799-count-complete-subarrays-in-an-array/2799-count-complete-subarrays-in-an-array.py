class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        ans = 0
        for i in range(len(nums)):
            seen = set()
            for j in range(i,len(nums)):
                seen.add(nums[j])

                if len(seen)==distinct:
                    ans+=len(nums)-j
                    break
                

        return ans            


        
           