class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        freq = {}
        n = len(s)
        mul = n//k
        for i in range(0,n,mul):
            x = s[i:i+mul]
            if x not in freq:
                freq[x] = 1
            else:
                freq[x]+=1


        for i in range(0,n,mul):
            y = t[i:i+mul]
            if y in freq:
                freq[y]-=1
                if freq[y]==0:
                    del freq[y]
            else:
                return False

        return True                

            


                  

        