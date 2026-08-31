class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3 = s1.split()
        s4 = s2.split()
        s = s3 + s4
        ans = []
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in freq:
            if freq[i]==1:
                ans.append(i)

        return ans        


             



        