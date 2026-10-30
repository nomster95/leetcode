class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for i in s:
            if i.isalpha():
                ans.append(i)
            else:
                if len(ans)!=0:
                    ans.pop()

        return "".join(ans)                

        