class Solution:
    def reverse(self,n):
        rev = 0
        while n>0:
            digit = n%10
            rev = rev*10 + digit
            n = n//10

        return rev

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = float('inf')

        freq = {}
        for i in range(len(nums)):
            rev = self.reverse(nums[i])

            if nums[i] not in freq:
                freq[rev] = i
            else:
                ans = min(ans,i-freq[nums[i]])
                freq[rev] = i
            
                  

        if ans==float('inf'):
            return -1        

        return ans          

    
        