class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        ans = set()
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in freq:
            if freq[i] not in ans:
                ans.add(freq[i])
            else:
                return False

        return True                   
        