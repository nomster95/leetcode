class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = []
        n = len(s)
        if n==1:
            return s
        for i in range(1,len(s)):
            ch = s[:i]
            rev = ch[::-1] + s[i:]
            ans.append(rev)
            ch_r = s[n-i-1:]
            rev_r = s[:n-i-1] + ch_r[::-1]
            ans.append(rev_r)

        ans.sort()
        return ans[0]    

        