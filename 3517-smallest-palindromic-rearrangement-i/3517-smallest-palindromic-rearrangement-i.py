class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        lst = list(s)
        p1 = lst[0:n//2]
        p1.sort()
        m = len(p1)
        mid = lst[(n-1)//2]
        if n==1:
            return s
        ans = [0]*n
        for i in range(m):
            if n%2!=0:
                ans[i] = p1[i]
                ans[(len(ans)-1)//2] = mid
                ans[i+m+1] = p1[m-i-1]
            else:
                ans[i] = p1[i]    
                ans[i+m] = p1[m-i-1]

        return "".join(ans)
        