class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            consistent = True
            for j in set(words[i]):
                if j not in allowed:
                    consistent = False

            if consistent:
                count+=1

        return count        




        
                    
        