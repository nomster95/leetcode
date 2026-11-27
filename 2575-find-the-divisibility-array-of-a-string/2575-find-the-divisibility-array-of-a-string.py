class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        ans = [0]*n
        r = 0
        for i in range(n):
            x = int(word[i])
            r = (r*10+x)%m
            if r==0:
                ans[i] = 1
            else:
                ans[i] = 0

        return ans            