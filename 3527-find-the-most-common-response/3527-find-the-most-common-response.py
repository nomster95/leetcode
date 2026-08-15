class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = {}
        for i in responses:
            survey = set(i)
            for j in survey:
                if j not in freq:
                    freq[j]=1
                else:
                    freq[j]+=1

        ans = sorted(freq.items(), key=lambda x: (-x[1], x[0]))     
        return ans[0][0]   




        