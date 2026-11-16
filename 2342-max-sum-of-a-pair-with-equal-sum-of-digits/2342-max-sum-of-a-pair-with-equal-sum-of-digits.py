class Solution:
    def sum_of_digits(self,n):
        sums = 0
        while n!=0:
            digit = n%10
            sums+=digit
            n = n//10

        return sums

    def maximumSum(self, nums: list[int]) -> int:
        max_sum = -1
        freq = {}
        for i in nums:
            sums = self.sum_of_digits(i)
            if sums not in freq:
                freq[sums] = i
            else:
                max_sum = max(max_sum,freq[sums]+i)
                if i>freq[sums]:
                    freq[sums] = i

        return max_sum            


        