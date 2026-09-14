class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = {}
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                pair = nums[i]*nums[j]
                ans+=freq.get(pair,0)*8

                freq[pair] = freq.get(pair,0)+1

        
        return ans





        