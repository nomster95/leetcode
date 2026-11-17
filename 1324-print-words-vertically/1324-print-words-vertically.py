class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        words = s.split(" ")
        max_len = 0
        for i in words:
            max_len = max(max_len,len(i))

        for i in range(max_len):
            word = ""
            for j in words:
                if i>=len(j):
                    word+=" "
                else:
                    word+=j[i]

            x = word.rstrip()        
            ans.append(x)

        return ans                


        