class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        freq = {}
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                if secret[i] not in freq:
                    freq[secret[i]] = 1
                else:
                    freq[secret[i]]+=1

        for i in range(len(secret)):
            if secret[i]!=guess[i]:

                if guess[i] in freq and freq[guess[i]]>0:
                    cows+=1
                    freq[guess[i]]-=1

        return f"{bulls}A{cows}B"        

       

        