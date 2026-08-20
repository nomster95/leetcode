class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        freq  = {}
        ans = []
        for i,x in enumerate(groupSizes):
            if x not in freq:
                freq[x] = []
            freq[x].append(i)

        for i in freq:
            for j in range(0,len(freq[i]),i):
                ans.append(freq[i][j:j+i])

        return ans        

        