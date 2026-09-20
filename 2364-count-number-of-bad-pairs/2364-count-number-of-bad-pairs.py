class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        freq = {}
        pairs = 0
        n = len(nums)
        good = 0
        total_pairs = (n*(n-1))//2
        for i in range(len(nums)):
            i_val = nums[i] - i
            if i_val not in freq:
                freq[i_val] = 1
            else:
                freq[i_val]+=1

        for i in freq.values():
            good+= (i*(i-1))//2

        return total_pairs - good    




        

                



        