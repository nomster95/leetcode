class Solution:
    def similarPairs(self, words: list[str]) -> int:
        ans = 0
        for i in range(len(words)):
            freq1 = {}
            for j in set(words[i]):
                if j not in freq1:
                    freq1[j] = 1
                else:
                    freq1[j]+=1

            for x in range(i+1,len(words)):
                freq2 = {}
                for y in set(words[x]):
                    if y not in freq2:
                        freq2[y] = 1
                    else:
                        freq2[y]+=1

                if freq1==freq2:
                    ans+=1

        return ans                    

                        




        