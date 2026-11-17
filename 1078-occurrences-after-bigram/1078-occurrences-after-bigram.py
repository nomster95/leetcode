class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split(" ")
        n = len(words)
        ans = []
        for i in range(n-1):
            if words[i]==first and words[i+1]==second and i+2<n:
                ans.append(words[i+2])

        return ans        


        