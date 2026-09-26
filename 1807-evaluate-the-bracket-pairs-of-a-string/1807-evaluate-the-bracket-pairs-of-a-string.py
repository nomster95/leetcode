class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        freq = {}
        key = ""
        ans = ""
        inside = False
        for x in knowledge:
            freq[x[0]] = x[1]

        for i in range(len(s)):
            if s[i]=="(":
                inside = True
                start = i+1
            elif s[i]==")":
                inside = False
                key = s[start:i]
                if key in freq:
                    ans+=freq[key]
                else:
                    ans+="?"

            elif not inside:
                ans+=s[i]

        return ans        




        



        
        