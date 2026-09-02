class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans , sol = [] , []
        def backtrack(i,curr_cost):
            if len(sol)==n:
                ans.append(''.join(sol))
                return

            if curr_cost>k:
                return


            sol.append('0')
            backtrack(i+1,curr_cost)
            sol.pop()

            if (len(sol)==0 or sol[-1]!='1') and (curr_cost + i)<=k:
                sol.append('1')
                backtrack(i+1,curr_cost + i)
                sol.pop()


        backtrack(0,0)
        return ans        

        