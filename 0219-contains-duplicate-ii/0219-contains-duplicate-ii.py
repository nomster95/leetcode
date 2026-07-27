class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]] = i
            else:
                diff = abs(i-freq[nums[i]])    
                if diff<=k:
                    return True
                else:

                    freq[nums[i]] = i

        return False            
                        
        