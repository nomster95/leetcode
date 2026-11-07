class Solution:
    def compress(self, chars) -> int:
        n = len(chars)
        current_char  = chars[0]
        count = 1
        ans = ""

        for i in range(1,len(chars)):
            if chars[i]==current_char:
                count+=1

            else:
                if count>1:
                    ans+=f"{count}{current_char}"
                else:
                    ans+=f"{'1'}{current_char}"  

                current_char = chars[i]
                count = 1

        if count>1:
            ans+=f"{count}{current_char}" 
        else:
            ans+=f"{1}{current_char}"     

        return ans

    def countAndSay(self, n: int) -> str:
        x = "1"
        for i in range(n-1):
            new_x = self.compress(x)
            x = new_x

        return x    


        