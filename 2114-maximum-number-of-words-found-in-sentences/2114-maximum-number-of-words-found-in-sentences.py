class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = []
        for i in sentences:
            m = i.split(" ")
            ans.append(len(m))

        return max(ans)
            

        