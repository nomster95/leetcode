class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = {}
        ans = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in freq:
            if freq[i]==1 and i+1 not in freq and i-1 not in freq:
                ans.append(i)

        return ans        

        