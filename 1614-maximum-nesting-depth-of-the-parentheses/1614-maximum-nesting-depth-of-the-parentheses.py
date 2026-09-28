class Solution:
    def maxDepth(self, s: str) -> int:
        max_par = 0
        opens = 0
        for i in s:
            if i=="(":
                opens+=1
                max_par = max(max_par,opens)
            elif i==")":
                opens-=1

        return max_par            


        