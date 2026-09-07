class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)
        l,r = 0,0
        g.sort()
        s.sort()
        while l<n and r<m:
            if s[r]>=g[l]:
                r+=1
                l+=1
            else:
                r+=1    

        return l     
        