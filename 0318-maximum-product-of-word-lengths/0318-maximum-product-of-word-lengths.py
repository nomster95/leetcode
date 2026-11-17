class Solution:
    def uncommon(self,s1,s2):
        seen = set(s1)
        
        for i in s2:
            if i in seen:
                return False

        return True

    def maxProduct(self, words: list[str]) -> int:
        max_product = 0
        n = len(words)
        for i in range(n):
            for j in range(i,n):
                if self.uncommon(words[i],words[j]):
                    max_product = max(max_product,len(words[i])*len(words[j]))

        return max_product            

        