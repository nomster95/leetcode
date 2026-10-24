class Solution:
    def minFlips(self, target: str) -> int:
        ops = 0
        flips = 0
        for i in range(len(target)):
            effect = int(target[i])^flips
            if effect==1:
                flips = 1-flips
                ops+=1

        return ops        
        