class Solution:
    def flips(self,s):
        new_bit = ""
        for i in s:
            if i=="1":
                new_bit+="0"
            else:
                new_bit+="1"

        return new_bit

    def findKthBit(self, n: int, k: int) -> str:
        s1 = "0"

        for i in range(n-1):
            
            new_s = s1 + "1" + self.flips(s1)[::-1]
            s1 = new_s


        return s1[k-1]    

        

        