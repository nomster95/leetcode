class Solution:
    def countValidSubstrings(self, s: str) -> int:
        l,r = 0,0
        count = 0
        seen = ""
        while r<len(s):
            seen+=s[r]

            if seen[r-2:r+1]=="abc":
                l = r-1

            count+=(r-l+1)
            r+=1

        return count        

        