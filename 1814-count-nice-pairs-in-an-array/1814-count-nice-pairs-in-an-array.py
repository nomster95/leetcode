class Solution:
    def rev(self,n):
        rev = 0
        while n!=0:
            digit = n%10
            rev = rev*10 + digit
            n = n//10

        return rev
    def countNicePairs(self, nums: list[int]) -> int:
        freq = {}
        modulo = (10**9) + 7
        for i in range(len(nums)):
            i_val = nums[i] - self.rev(nums[i])
            if i_val not in freq:
                freq[i_val] = 1
            else:
                freq[i_val]+=1

        good  = 0
        for i in freq.values():
            good += (i*(i-1))//2

        return good%modulo               
        