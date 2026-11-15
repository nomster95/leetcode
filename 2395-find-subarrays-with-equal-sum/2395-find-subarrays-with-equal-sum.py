class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        l = 0
        r = 2
        seen = set()
        sums = sum(nums[:2])
        seen.add(sums)

        while r<len(nums):
            sums+=nums[r]
            sums-=nums[l]

            if sums in seen:
                return True
            else:
                seen.add(sums)    

            r+=1
            l+=1

        return False        

        
        