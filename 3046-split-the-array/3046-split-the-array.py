class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for j in freq:
            if freq[j]>2:
                return False

        return True                    
        