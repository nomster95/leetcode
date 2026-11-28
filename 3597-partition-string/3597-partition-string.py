class Solution:
    def partitionString(self, s: str) -> List[str]:
        ans = []
        seen = set()
        i = 0
        new = ""
        while i<len(s):
            new+=s[i]
            if new not in seen:
                ans.append(new)
                seen.add(new)
                new = ""
            
            i+=1    

              

        return ans        





        


        