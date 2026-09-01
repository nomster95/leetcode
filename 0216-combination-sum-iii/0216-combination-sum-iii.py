class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans , sol = [] ,  []
        def backtrack(i,curr_sum,count):
            if curr_sum==n and count==k:
                ans.append(sol[:])
                return

            if curr_sum>n or count>k or i>9:
                return

            backtrack(i+1,curr_sum,count)
            sol.append(i)
            backtrack(i+1,curr_sum + i,count+1)
            sol.pop()

        backtrack(1,0,0)
        return ans    




        