class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans , sol = [] , []
        def backtrack():
            if len(sol)==n:
                ans.append(''.join(sol))
                return

            for ch in "abc":
                if len(sol)==0 or ch!=sol[-1]:
                    sol.append(ch)
                    backtrack()
                    sol.pop()   


        backtrack()
        if k>len(ans):
            return ""

        return ans[k-1]    


        