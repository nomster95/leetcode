class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans , sol = [] , []
        freq = {}
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x]+=1

        def backtrack():
            if len(sol)==n:
                ans.append(sol[:])
                return

            for x in freq:
                if freq[x]>0:
                    sol.append(x)
                    freq[x]-=1

                    backtrack()
                    freq[x]+=1
                    sol.pop()

        backtrack()
        return ans            



        