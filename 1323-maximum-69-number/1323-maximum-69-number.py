class Solution:
    def maximum69Number (self, num: int) -> int:
        x = str(num)
        limit = 1
        ans = ""
        for i in x:
            if i=="6" and limit>0:
                ans+="9"
                limit-=1
            else:
                ans+=i

        return int(ans)            
        