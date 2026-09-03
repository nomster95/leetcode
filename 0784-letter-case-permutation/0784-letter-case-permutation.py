class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans , sol = [] , []
        n = len(s)
        def backtrack(i):
            if len(sol)==n:
                ans.append(''.join(sol))
                return

            if s[i].isdigit():
                sol.append(s[i])
                backtrack(i+1)
                sol.pop()

            else:
                sol.append(s[i].upper())
                backtrack(i+1)
                sol.pop()

                sol.append(s[i].lower())
                backtrack(i+1)
                sol.pop()
                
                        

             



        backtrack(0)
        return ans       

        