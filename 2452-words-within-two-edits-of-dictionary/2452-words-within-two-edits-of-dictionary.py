class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        ans = []
        for ch in queries:
            word = ch
            for i in dictionary:
                edits = 0
                x = i
                for j in range(len(x)):
                    if word[j]!=x[j]:
                        edits+=1

                if edits<=2:
                    ans.append(word)
                    break

        return ans                    




        
        