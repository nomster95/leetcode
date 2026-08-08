class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        space = set(spaces)
        
        for i in range(len(s)):
            if i in space:
                ans+=" "

            ans+=s[i]   
        
        return ans