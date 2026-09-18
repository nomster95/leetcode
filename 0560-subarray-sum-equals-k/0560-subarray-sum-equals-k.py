class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        prefix = 0
        count = 0
        for i in nums:
            prefix+=i

            needed = prefix-k
            if needed in freq:
                count+=freq[needed]

            freq[prefix] = freq.get(prefix,0)+1    
        
        return count