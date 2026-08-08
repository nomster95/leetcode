class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ["999","888","777","666","555","444","333","222","111","000"]
        l = 0
        while l<len(ans):
            if ans[l] not in  num:
                l+=1
                
            else:
                return ans[l] 

        return ""        