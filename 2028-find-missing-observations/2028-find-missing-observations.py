class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        remsum = (mean*(n+m))-sum(rolls)
        x = remsum//n
        y = remsum%n
        if x>6 or x<1:
            return []
        elif x==6 and y>0:
            return []

        ans = [x]*n
        for i in range(y):
            ans[i] = x+1

        return ans        


        