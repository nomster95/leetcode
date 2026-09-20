class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = {}
        good = 0
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]]+=1

        for i in freq.values():
            good+= (i*(i-1))//2

        return good                

        
        