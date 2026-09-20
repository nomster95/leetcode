class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        spam = 0
        banned = set(bannedWords)
        for i in message:
           if i in banned:
            spam+=1

        if spam>=2:
            return True

        return False        