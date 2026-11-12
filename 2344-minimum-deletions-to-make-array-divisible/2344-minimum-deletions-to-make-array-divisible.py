import math
class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        hcf = math.gcd(*numsDivide)
        deletions = 0
        nums.sort()
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for x in sorted(set(nums)):
            if hcf%x==0:
                return deletions
            else:
                deletions+=freq[x]

        return -1                        
        