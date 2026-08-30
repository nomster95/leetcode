class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res , sol = [] , []
        n = len(candidates)
        

        def backtrack(i,curr_sum):
            if curr_sum==target:
                res.append(sol[:])
                return 

            if curr_sum>target:
                return

            for x in range(i, n):
                if x > i and candidates[x] == candidates[x - 1]:
                    continue

                sol.append(candidates[x])
                backtrack(x+1,curr_sum + candidates[x])
                sol.pop()

        candidates.sort()        
        backtrack(0,0)
        return res            


        