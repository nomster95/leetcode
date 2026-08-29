class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        ans = ""
        for x in s:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x]+=1

        for i in order:  
            if i in freq:
                while freq[i]!=0:
                    ans+=i
                    freq[i]-=1

        for i in freq:
            while freq[i]!=0:
                ans+=i
                freq[i]-=1

        return ans        





        