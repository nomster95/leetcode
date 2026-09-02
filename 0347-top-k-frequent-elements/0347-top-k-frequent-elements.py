class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        sol = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        ans = sorted(freq.items(),  key = lambda x: x[1] , reverse = True)
        for i in ans:
            sol.append(i[0])

        return sol[0:k]    


        