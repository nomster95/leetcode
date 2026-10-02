class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans = ""
        for i in s:
            if i=="(":
                count+=1
                if count>1:
                    ans+=i
            else:
                count-=1
                if count>0:
                    ans+=i

        return ans            


        