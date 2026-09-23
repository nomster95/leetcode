class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = {}
        ans = []
        for i in str(n):
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        max_freq = min(freq.values())        

        for x in freq:
            if freq[x]==max_freq:
                ans.append(int(x))

        return min(ans)        


           