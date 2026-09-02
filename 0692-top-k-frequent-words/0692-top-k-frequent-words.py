class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        sol = []
        for i in words:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        ans = sorted(freq.items(), key = lambda x:(-x[1],x[0]))   
        for i in ans:
            sol.append(i[0])

        return sol[0:k]    

                
        