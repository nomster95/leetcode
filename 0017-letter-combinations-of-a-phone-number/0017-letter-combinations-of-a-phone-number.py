class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans , sol = [] , []
        n = len(digits)
        phone_booth = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def backtrack(i):
            if i==n:
                ans.append(''.join(sol))
                return

            for ch in phone_booth[digits[i]]:
                sol.append(ch)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return ans    



        