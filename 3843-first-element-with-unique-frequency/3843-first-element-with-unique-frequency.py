class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq = {}
        freqCount = {}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        for i in freq:
            if freq[i] not in freqCount:
                freqCount[freq[i]] = 1
            else:
                freqCount[freq[i]]+=1

        for i in nums:
            if freqCount[freq[i]]==1:
                return i

        return -1            



        