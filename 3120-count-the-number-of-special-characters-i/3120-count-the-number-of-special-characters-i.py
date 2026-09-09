class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = set(word)
        seen = set()
        special = 0
        for i in word:
            if i.islower():
                seen.add(i)

        for i in seen:
            if i.upper() in ans:
                special+=1

        return special        

    

        