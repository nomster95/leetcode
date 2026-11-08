class Solution:
    def countValidSubstrings(self, s: str) -> int:
        l,r = 0,0
        count = 0
        a = -1
        ab = -1
        while r<len(s):
            if s[r]=="a":
                a = r
            elif s[r]=="b":
                if a!=-1:
                    ab = a

            else:
                if ab!=-1:
                    l = max(l,ab+1)

            count+=(r-l+1)
            r+=1

        return count                       

        