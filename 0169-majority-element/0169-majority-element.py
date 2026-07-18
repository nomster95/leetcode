class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
        for i in freq:
            if(freq[i]>n/2):
                return i            
