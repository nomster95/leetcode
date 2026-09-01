class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans , sol  = [] ,  []
        def backtrack(i):
            if len(sol)==n:
                ans.append(''.join(sol))
                return

            sol.append('1')
            backtrack(i+1)
            sol.pop()

            if len(sol)==0 or sol[i-1]!='0':
                sol.append('0')
                backtrack(i+1)
                sol.pop()

        backtrack(0)   
        return ans     

        