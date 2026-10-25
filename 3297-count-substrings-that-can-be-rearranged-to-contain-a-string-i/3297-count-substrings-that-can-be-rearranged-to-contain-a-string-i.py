class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        count = 0
        l,r = 0,0
        formed = 0
        freq1 = {}
        for i in word2:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i]+=1

        freq2 = {}
        while r<len(word1):
            if word1[r] not in freq2:
                freq2[word1[r]] = 1
            else:
                freq2[word1[r]]+=1

            if word1[r] in freq1 and freq1[word1[r]]==freq2[word1[r]]:
                formed+=1

            while formed==len(freq1):
                count+=len(word1)-r

                if word1[l] in freq1 and freq1[word1[l]]==freq2[word1[l]]:
                    formed-=1

                freq2[word1[l]]-=1
                l+=1

            r+=1    

        return count           





        