class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = 0
        for ch in stones:
            if(ch in jewels):
                jewel+=1

        return jewel        

        