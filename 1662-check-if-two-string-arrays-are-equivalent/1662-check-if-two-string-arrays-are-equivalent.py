class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res1 = ""
        res2 = ""
        for i in word1:
            res1+=i
        for i in word2:
            res2+=i

        if res1==res2:
            return True

        return False    



        