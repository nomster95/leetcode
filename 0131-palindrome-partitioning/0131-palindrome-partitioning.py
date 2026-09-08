class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans , sol = [] , []
        n = len(s)
        def backtrack(start):
            if start==n:
                ans.append(sol[:])
                return

            for end in range(start,n):
                if s[start:end+1] == s[start:end+1][::-1]:
                    sol.append(s[start:end+1])
                    backtrack(end+1)
                    sol.pop()

        backtrack(0)
        return ans            


        