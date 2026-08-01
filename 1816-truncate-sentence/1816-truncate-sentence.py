class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        m = s.split()
        ans = m[0:k]
        return " ".join(ans)
        