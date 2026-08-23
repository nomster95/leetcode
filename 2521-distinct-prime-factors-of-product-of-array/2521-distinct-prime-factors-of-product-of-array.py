class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()
        for i in nums:
            n = 2
            while i!=1:
                if i%n!=0:
                    n+=1
                else:
                    i = i//n
                    ans.add(n)

        return len(ans)                


                
        