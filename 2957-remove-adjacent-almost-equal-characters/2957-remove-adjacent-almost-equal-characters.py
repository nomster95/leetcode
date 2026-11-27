class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        ops = 0
        n = len(word)
        x = list(word)
        for i in range(n-1):
            if ord(x[i])==ord(x[i+1]) or abs(ord(x[i])-ord(x[i+1]))==1:
                x[i+1] = "#"
                ops+=1

        return ops        
        