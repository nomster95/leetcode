class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        ans = []
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in freq:
            if freq[i]==1:
                ans.append(i)

        if len(ans)<k:
            return ""

        return ans[k-1]                    


        