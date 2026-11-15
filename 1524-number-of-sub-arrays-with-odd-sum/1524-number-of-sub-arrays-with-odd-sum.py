class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        prefix = 0
        count = 0
        freq = {0:1}
        n = len(arr)
        mod = 10**9 + 7
        for i in arr:
            prefix+=i

            rem = prefix%2
            if rem in freq:
                count+=freq[rem]

            freq[prefix%2] = freq.get(prefix%2,0) + 1

        ans =  (n*(n+1))//2 - count   
        return ans%mod 


        