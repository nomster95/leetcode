class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans , sol = [] , []
        res = set(nums)
        n = len(nums)
        def backtrack(i):
            if len(sol)==n:
                ans.append(''.join(sol))
                return

            sol.append('1')
            backtrack(i+1)
            sol.pop()

            sol.append('0')
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        for i in ans:
            if i not in res:
                return i

        