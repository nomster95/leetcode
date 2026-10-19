class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1    
        return len(nums) - max(freq.values())
        