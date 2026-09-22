class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans = ""
        for i in words:
            ans+=i[0]

        if ans==s:
            return True

        return False    

       
             

        