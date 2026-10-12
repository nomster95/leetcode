class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        ones = 0
        zeroes = 0
        for i in t:
            if i=="1":
                ones+=1

        zeroes = len(t)-ones
        ans = ""
        for i in s:
            if i=="0":
                if ones>0:
                    ans+="1"
                    ones-=1
                else:
                    ans+="0"
                    zeroes-=1
            else:
                if zeroes>0:
                    ans+="0"
                    zeroes-=1
                else:
                    ans+="1"
                    ones-=1

        si = int(s,2)
        ansi = int(ans,2)
        final = si ^ ansi
        return bin(final)[2:].zfill(len(s))                                  
        