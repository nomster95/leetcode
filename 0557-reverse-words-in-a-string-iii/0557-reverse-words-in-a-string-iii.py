class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        t = s.split()
        for i in t:
            ch = i[::-1]
            ans.append(ch)

        return " ".join(ans)    

        