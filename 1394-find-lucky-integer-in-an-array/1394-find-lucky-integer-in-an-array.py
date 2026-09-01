class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        ans = []
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in freq:
            if freq[i]==i:
                ans.append(i)

        if len(ans)==0:
            return -1

        return max(ans)                    


        