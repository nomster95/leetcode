class Solution:
    def f(self,s):
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        min_c = s[0]
        min_freq = freq[s[0]]
        for i in freq:
            if i<min_c:
                min_c = i
                min_freq = freq[i]

        return min_freq                     
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        freq_arr = []
        for i in words:
            count = self.f(i)
            freq_arr.append(count)

        ans = [0]*len(queries)
        for x in range(len(queries)):
            y = self.f(queries[x])
            final = 0
            for j in freq_arr:
                if j>y:
                    final+=1
            ans[x] = final

        return ans                

        