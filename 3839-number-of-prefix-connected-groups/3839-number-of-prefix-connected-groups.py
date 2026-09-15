class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        freq = {}
        ans = 0
        for i in words:
            if len(i)>=k:
                if i[0:k] not in freq:
                    freq[i[0:k]] = 1
                else:
                    freq[i[0:k]]+=1

        for i in freq:
            if freq[i]>1:
                ans+=1

        return ans        






                

        