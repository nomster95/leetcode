class Solution:
    def minSwaps(self, s: str) -> int:
        ans = list(s)
        j = len(s)-1
        opening = 0
        closing = 0
        ops = 0
        for i in range(len(s)):
            if ans[i]=="]" and closing>=opening:
                while j>=0 and ans[j]!="[":
                    j-=1
                ans[i],ans[j] = ans[j],ans[i]    
                ops+=1

            if ans[i]=="[":
                opening+=1
            else:
                closing+=1   

        return ops         
        