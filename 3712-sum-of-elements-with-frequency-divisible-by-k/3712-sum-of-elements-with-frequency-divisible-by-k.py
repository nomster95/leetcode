class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = {}
        ans = 0
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        for i in nums:
            if freq[i]%k==0:
                ans+=i

        return ans        


        