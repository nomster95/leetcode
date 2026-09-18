class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix = 0
        count = 0
        freq = {0:1}
        for i in nums:
            prefix+=i

            rem = prefix%k
            if rem in freq:
                count+=freq[rem]

            freq[prefix%k] = freq.get(prefix%k,0) + 1

        return count        

        